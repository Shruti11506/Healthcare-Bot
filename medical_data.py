# medical_data.py
# Compressed medical knowledge base - symptoms, treatments, and FAQs
# This compression technique reduces token usage while maintaining accuracy

MEDICAL_KNOWLEDGE_BASE = {
    "symptoms": {
        "fever": {
            "description": "Body temperature above 38°C (100.4°F)",
            "causes": ["Infection (viral/bacterial)", "Inflammation", "Heat exhaustion", "Medication side effects"],
            "treatments": ["Rest", "Hydration (8-10 glasses water)", "Paracetamol/Ibuprofen for adults", "Cool compress"],
            "seek_doctor": ["Temp above 39.5°C", "Lasts more than 3 days", "Severe headache with stiff neck", "Difficulty breathing"],
            "severity": "medium"
        },
        "headache": {
            "description": "Pain or discomfort in the head or neck area",
            "causes": ["Tension", "Dehydration", "Migraine", "Sinusitis", "High blood pressure"],
            "treatments": ["Rest in dark quiet room", "Hydration", "OTC pain relievers", "Cold/warm compress"],
            "seek_doctor": ["Sudden severe ('thunderclap') headache", "Headache with fever and stiff neck", "After head injury", "Vision changes"],
            "severity": "low-medium"
        },
        "cold": {
            "description": "Viral infection of the upper respiratory tract",
            "causes": ["Rhinovirus (most common)", "Coronavirus", "RSV"],
            "treatments": ["Rest", "Fluids", "Honey-lemon-ginger tea", "Steam inhalation", "Saline nasal drops"],
            "seek_doctor": ["Symptoms worsen after 7-10 days", "High fever", "Chest pain", "Difficulty breathing"],
            "severity": "low"
        },
        "cough": {
            "description": "Reflex action to clear the throat and airways",
            "causes": ["Common cold", "Allergies", "Asthma", "GERD", "Smoking"],
            "treatments": ["Honey (adults)", "Steam inhalation", "Stay hydrated", "Cough drops", "Elevate head while sleeping"],
            "seek_doctor": ["Coughing blood", "Lasts more than 3 weeks", "Shortness of breath", "Chest pain"],
            "severity": "low-medium"
        },
        "stomach_pain": {
            "description": "Discomfort or pain in the abdominal area",
            "causes": ["Indigestion", "Gas", "Food poisoning", "IBS", "Appendicitis"],
            "treatments": ["BRAT diet (Bananas, Rice, Applesauce, Toast)", "Avoid spicy/fatty foods", "Antacids", "Ginger tea"],
            "seek_doctor": ["Severe sudden pain", "Pain with fever", "Blood in stool", "Pain lasting more than 2 days"],
            "severity": "medium"
        },
        "diarrhea": {
            "description": "Loose or watery stools occurring frequently",
            "causes": ["Food poisoning", "Viral infection", "IBS", "Antibiotic use", "Food intolerance"],
            "treatments": ["ORS (Oral Rehydration Solution)", "BRAT diet", "Avoid dairy/fatty foods", "Probiotics"],
            "seek_doctor": ["Bloody stool", "Dehydration signs", "Lasts more than 2 days (adults)", "High fever"],
            "severity": "medium"
        },
        "fatigue": {
            "description": "Extreme tiredness not relieved by rest",
            "causes": ["Poor sleep", "Anemia", "Thyroid issues", "Depression", "Diabetes", "Dehydration"],
            "treatments": ["Improve sleep hygiene", "Regular exercise", "Balanced diet", "Limit caffeine", "Stay hydrated"],
            "seek_doctor": ["Severe unexplained fatigue", "With other symptoms", "Affecting daily life", "Sudden onset"],
            "severity": "low-medium"
        },
        "sore_throat": {
            "description": "Pain, scratchiness or irritation of the throat",
            "causes": ["Strep throat", "Viral infection", "Allergies", "Dry air", "GERD"],
            "treatments": ["Salt water gargle", "Warm honey-lemon water", "OTC throat lozenges", "Rest voice", "Stay hydrated"],
            "seek_doctor": ["Difficulty swallowing or breathing", "High fever", "Pus/white patches on tonsils", "Lasts more than 1 week"],
            "severity": "low-medium"
        },
        "rash": {
            "description": "Change in skin texture or color",
            "causes": ["Allergic reaction", "Eczema", "Contact dermatitis", "Viral infection", "Heat"],
            "treatments": ["Identify and avoid trigger", "Calamine lotion", "Antihistamines", "Cool compress", "Moisturize"],
            "seek_doctor": ["Spreads rapidly", "With fever", "Painful or blistering", "On face/genitals"],
            "severity": "medium"
        },
        "back_pain": {
            "description": "Pain in the lower, middle, or upper back",
            "causes": ["Muscle strain", "Poor posture", "Herniated disc", "Arthritis", "Kidney issues"],
            "treatments": ["Rest (not bed rest)", "Ice/heat therapy", "Gentle stretching", "OTC pain relievers", "Posture correction"],
            "seek_doctor": ["Pain down the leg", "Numbness/tingling", "After injury", "With fever or weight loss"],
            "severity": "medium"
        }
    },
    "general_health_tips": [
        "Drink 8 glasses of water daily",
        "Sleep 7-9 hours per night",
        "Exercise 30 minutes most days",
        "Eat a balanced diet with fruits and vegetables",
        "Wash hands frequently to prevent infections",
        "Avoid smoking and limit alcohol",
        "Manage stress through meditation or hobbies",
        "Get regular health check-ups"
    ],
    "emergency_symptoms": [
        "Chest pain or pressure",
        "Difficulty breathing",
        "Signs of stroke (face drooping, arm weakness, speech difficulty)",
        "Severe allergic reaction",
        "Loss of consciousness",
        "Severe bleeding",
        "High fever with stiff neck and rash",
        "Suspected poisoning"
    ],
    "disclaimer": "This information is for educational purposes only and does not replace professional medical advice. Always consult a qualified healthcare provider for diagnosis and treatment."
}

def get_compressed_context():
    """
    Returns a compressed version of the medical knowledge base
    formatted as a concise string to minimize token usage
    while preserving essential information.
    """
    symptoms_compressed = []
    for symptom, data in MEDICAL_KNOWLEDGE_BASE["symptoms"].items():
        entry = f"""
[{symptom.upper()}]
Causes: {', '.join(data['causes'][:3])}
Treatments: {', '.join(data['treatments'][:3])}
See Doctor If: {', '.join(data['seek_doctor'][:2])}"""
        symptoms_compressed.append(entry)

    emergency = ", ".join(MEDICAL_KNOWLEDGE_BASE["emergency_symptoms"][:5])
    
    compressed = f"""MEDICAL FAQ DATABASE (Compressed):
{''.join(symptoms_compressed)}

EMERGENCY (Call 911/108): {emergency}

DISCLAIMER: Educational only. Not a substitute for professional medical advice."""
    
    return compressed

def find_relevant_symptoms(query):
    """Find symptoms relevant to the user's query to further reduce tokens"""
    query_lower = query.lower()
    relevant = {}
    
    keyword_map = {
        "fever": ["fever", "temperature", "hot", "chills"],
        "headache": ["headache", "head pain", "migraine", "head hurts"],
        "cold": ["cold", "runny nose", "sneezing", "congestion"],
        "cough": ["cough", "coughing", "throat"],
        "stomach_pain": ["stomach", "abdominal", "belly", "tummy"],
        "diarrhea": ["diarrhea", "loose stool", "watery stool"],
        "fatigue": ["tired", "fatigue", "exhausted", "weakness", "energy"],
        "sore_throat": ["sore throat", "throat pain", "throat"],
        "rash": ["rash", "skin", "itching", "hives"],
        "back_pain": ["back pain", "back ache", "lower back"]
    }
    
    for symptom, keywords in keyword_map.items():
        if any(kw in query_lower for kw in keywords):
            relevant[symptom] = MEDICAL_KNOWLEDGE_BASE["symptoms"][symptom]
    
    return relevant if relevant else MEDICAL_KNOWLEDGE_BASE["symptoms"]
