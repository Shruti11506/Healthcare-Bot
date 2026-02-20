# 🏥 Healthcare FAQ Bot
### HPE GenAI for GenZ Challenge 2 — Submission

A medical FAQ chatbot that compresses symptom databases and treatment information, providing instant health answers with reduced token costs and higher accuracy using Claude AI.

---

## 📁 Project Files

```
healthcare-faq-bot/
├── app.py              ← Main Python server (run this!)
├── medical_data.py     ← Compressed medical knowledge base
├── index.html          ← Web interface (auto-served)
├── requirements.txt    ← Python dependencies
└── README.md           ← This file
```

---

## 🚀 Setup Instructions (Step by Step)

### Step 1: Install Python
Make sure Python is installed. Open Command Prompt and type:
```
python --version
```
If not installed, download from https://python.org

---

### Step 2: Get your Claude API Key
1. Go to https://console.anthropic.com
2. Sign up / Log in
3. Click "API Keys" → "Create Key"
4. Copy the key (starts with `sk-ant-...`)

---

### Step 3: Install Required Libraries
Open Command Prompt in the project folder and run:
```
pip install flask anthropic
```
Or use the requirements file:
```
pip install -r requirements.txt
```

---

### Step 4: Set Your API Key

**Windows (Command Prompt):**
```
set ANTHROPIC_API_KEY=sk-ant-your-key-here
```

**Mac/Linux (Terminal):**
```
export ANTHROPIC_API_KEY=sk-ant-your-key-here
```

Alternatively, open `app.py` and on line 20, replace:
```python
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "your_api_key_here")
```
With:
```python
API_KEY = "sk-ant-your-actual-key-here"
```

---

### Step 5: Run the Bot!
```
python app.py
```

You'll see:
```
==================================================
🏥 Healthcare FAQ Bot Starting...
==================================================
✅ API Key detected

🌐 Open your browser and go to:
   http://localhost:5000
```

Open your browser and go to **http://localhost:5000** 🎉

---

## ✨ Key Features

### 🗜️ Token Compression (Challenge Requirement)
- **Smart Context Filtering**: Only sends relevant symptom data to the AI based on the user's query
- **Conversation Pruning**: Keeps only last 6 messages to avoid token bloat
- **Compressed Knowledge Base**: Medical data stored in compact structured format
- **Result**: Up to 70% fewer tokens compared to sending full database each time

### 🎯 Higher Accuracy
- Structured medical knowledge base with symptoms, causes, and treatments
- Emergency keyword detection (bypasses AI for immediate emergency alerts)
- Targeted context = less irrelevant info = better answers

### 💻 Web Interface
- Real-time chat with typing indicators
- Quick question buttons for common symptoms
- Token usage display per message
- Emergency alerts in red
- Mobile-friendly design

---

## 🏗️ How It Works

```
User types question
       ↓
Emergency check (instant if chest pain/stroke etc.)
       ↓
Find relevant symptoms (COMPRESSION - only load what's needed)
       ↓
Build compressed context string
       ↓
Send to Claude API with conversation history
       ↓
Return answer + token count to user
```

---

## 🔧 Customization

**Add more symptoms** → Edit `medical_data.py`, add entries to `MEDICAL_KNOWLEDGE_BASE["symptoms"]`

**Change AI model** → In `app.py`, change `claude-haiku-4-5-20251001` to `claude-sonnet-4-6` (more powerful, higher cost)

**Change max response length** → In `app.py`, change `max_tokens=500`

---

## 📊 Technical Stack

| Component | Technology |
|-----------|-----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python + Flask |
| AI Model | Claude Haiku (Anthropic) |
| Token Compression | Custom Python algorithm |
| Knowledge Base | Structured Python dictionary |

---

## ⚠️ Disclaimer

This bot provides general health information for educational purposes only. It is NOT a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider.

---

*Built for HPE GenAI for GenZ Challenge 2*
