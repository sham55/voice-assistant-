# 🎙️ Voice-Activated ChatGPT Assistant

This is a simple **voice assistant** (like Jarvis) built with:
- Python
- OpenAI GPT API
- SpeechRecognition (Google STT)
- pyttsx3 (TTS)

---

## 🚀 Features
✅ Wake word detection ("Hey")  
✅ Talks back using text-to-speech  
✅ Uses GPT-4 / GPT-3.5 for answers  
✅ Stops when you say "stop"  

---

## 🔧 Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/sham55/voice-assistant.git
   cd voice-assistant

Create a virtual environment:

python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Add your OpenAI API key:

Create a .env file:

OPENAI_API_KEY=your_api_key_here


Run the assistant:

python voice_assistant.py

📦 Requirements

Python 3.8+

openai

python-dotenv

speechrecognition

pyttsx3

pyaudio (for microphone input)

numpy

Install them with:

pip install openai python-dotenv SpeechRecognition pyttsx3 pyaudio numpy

