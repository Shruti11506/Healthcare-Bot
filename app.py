# app.py
from flask import Flask, request, jsonify, send_file
import os
import google.genai as genai
from medical_data import find_relevant_symptoms, get_compressed_context, MEDICAL_KNOWLEDGE_BASE
import time

# ========= CONFIGURE API KEY =========
# Uses environment variable if set, otherwise falls back to the provided key.
API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyBfIa566QWb2NxZVHGfXeeUccET-RKcCOo")

if API_KEY:
    client = genai.Client(http_options={'api_version': 'v1alpha'}, api_key=API_KEY)
    print("Gemini API Key detected. Running in LIVE mode.")
else:
    client = None
    print("WARNING: GEMINI_API_KEY not set. Running in MOCK mode.")
    print("To use the real AI, please set your GEMINI_API_KEY environment variable.")

# ========= SYSTEM PROMPT =========
SYSTEM_INSTRUCTION = """
You are MediBot, a friendly Healthcare FAQ Assistant.

Rules:
1. Be empathetic and caring.
2. Keep answers concise.
3. Structure: What it might be -> Home remedies -> When to see a doctor.
4. Always advise consulting a real doctor for serious issues.
5. For emergencies (chest pain, stroke, breathing difficulty), say call 911/108 immediately.
6. Only use the medical context provided to answer the user's health question.
"""

# Store chat sessions
sessions = {}

class MockChatSession:
    def send_message(self, prompt):
        time.sleep(1.5) # Simulate API latency
        class MockResponse:
            text = "*(Mock Mode Active)* I am currently running without an API key. \n\nIf you had provided a Gemini API Key, I would have analyzed the medical context and informed you about potential causes, treatments, and when to seek medical help based on your query.\n\nTo enable the real AI, stop the server and set the `GEMINI_API_KEY`."
        return MockResponse()

# ========= FLASK APP =========
app = Flask(__name__)

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        message = data.get("message", "")
        session_id = data.get("session_id", "default")

        if not message:
            return jsonify({"error": "Empty message"}), 400

        # Initialize chat session if it doesn't exist
        if session_id not in sessions:
            if client:
                 sessions[session_id] = client.chats.create(
                    model="gemini-2.5-flash",
                    config=genai.types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION
                    )
                 )
            else:
                 sessions[session_id] = MockChatSession()

        chat_session = sessions[session_id]
        
        # 1. Retrieve relevant symptoms based on user query
        relevant_data = find_relevant_symptoms(message)
        
        # 2. Build compressed context string for this specific turn
        context_parts = []
        for symptom, s_data in relevant_data.items():
            entry = f"[{symptom.upper()}] Causes: {', '.join(s_data['causes'][:3])} | Treatments: {', '.join(s_data['treatments'][:3])} | Doctor: {', '.join(s_data['seek_doctor'][:2])}"
            context_parts.append(entry)
            
        emergency_list = ", ".join(MEDICAL_KNOWLEDGE_BASE["emergency_symptoms"][:5])
        context_str = f"CONTEXT:\nRelevant FAQs:\n" + "\n".join(context_parts) + f"\nEMERGENCIES: {emergency_list}"
        
        context_tokens = len(context_str.split())
        
        # 3. Check for emergency keywords in the message
        is_emergency = any(word in message.lower() for word in ["chest pain", "heart", "stroke", "breathing", "breath", "unconscious", "bleed", "blood"])
        
        # 4. Construct prompt with context
        prompt_with_context = f"User Message: {message}\n\n{context_str}\n\nPlease answer the user based on the context."

        # 5. Send message
        response = chat_session.send_message(prompt_with_context)
        
        # 6. Calculate token usage roughly
        total_tokens = len(prompt_with_context.split()) * 1.3 + len(response.text.split()) * 1.3

        return jsonify({
            "response": response.text,
            "tokens_used": int(total_tokens),
            "context_tokens": context_tokens,
            "is_emergency": is_emergency
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route("/reset", methods=["POST"])
def reset():
    data = request.get_json()
    session_id = data.get("session_id", "default")
    if session_id in sessions:
        sessions.pop(session_id, None)
    return jsonify({"status": "cleared"}), 200

if __name__ == "__main__":
    print("Starting Healthcare Bot...")
    app.run(debug=True, port=5000)
