import os
import openai
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3
import numpy as np

# -----------------------------
#  Load Environment Variables
# -----------------------------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("⚠️ OPENAI_API_KEY not found in .env file")

# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)

# -----------------------------
#  Configuration
# -----------------------------
MODEL = "gpt-4"   # Change to "gpt-3.5-turbo" if needed
ASSISTANT_NAME = "Sham"

# -----------------------------
#  Text-to-Speech Setup
# -----------------------------
engine = pyttsx3.init()
voices = engine.getProperty("voices")

# Pick a different voice if available
if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)

# -----------------------------
#  Greetings
# -----------------------------
greetings = [
    f"What's up master {ASSISTANT_NAME}!",
    "Yeah?",
    f"Ahoy there, Captain {ASSISTANT_NAME}!",
    f"Bonjour, Monsieur {ASSISTANT_NAME}! Comment ça va?",
]

# -----------------------------
#  Functions
# -----------------------------
def speak(text: str):
    """Speak text aloud using pyttsx3"""
    print(f"🤖 ChatGPT: {text}")
    engine.say(text)
    engine.runAndWait()


def listen_for_wake_word(source):
    """Listen for the wake word 'hey'"""
    print("🎤 Listening for wake word: 'Hey'...")

    while True:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio).lower()

            if "hey" in text:
                print("✅ Wake word detected!")
                speak(np.random.choice(greetings))
                listen_and_respond(source)
                break

        except sr.UnknownValueError:
            pass  # Ignore noise or unrecognized speech
        except sr.RequestError as e:
            print(f"⚠️ Speech recognition error: {e}")
            break


def listen_and_respond(source):
    """Listen to user input and respond via ChatGPT"""
    print("🎤 Listening for your question... (say 'stop' to exit)")

    while True:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(f"🗣️ You said: {text}")

            if "stop" in text.lower():
                speak("Okay, shutting down. Goodbye!")
                break

            # Send to OpenAI GPT model
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": "You are a helpful voice assistant."},
                    {"role": "user", "content": text},
                ],
                max_tokens=150,
            )

            response_text = response.choices[0].message.content.strip()
            speak(response_text)

        except sr.UnknownValueError:
            print("❌ Could not understand. Please try again.")
        except sr.RequestError as e:
            print(f"⚠️ API error: {e}")
            speak("Sorry, I can't process your request right now.")
            break


# -----------------------------
#  Main
# -----------------------------
if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        listen_for_wake_word(source)
