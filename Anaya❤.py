print("INITIALIZING YOUR  ANAYA.... ")

import speech_recognition as sr
import webbrowser
import requests
import pygame
import os

import musicLibrary

from gtts import gTTS
from openai import OpenAI


# -----------------------------
# CONFIGURATION
# -----------------------------

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# -----------------------------
# TEXT TO SPEECH
# -----------------------------

def speak(text):
    print("Anaya:", text)

    try:
        tts = gTTS(text=text, lang="en")
        tts.save("temp.mp3")

        pygame.mixer.init()
        pygame.mixer.music.load("temp.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()
        pygame.mixer.quit()

        if os.path.exists("temp.mp3"):
            os.remove("temp.mp3")

    except Exception as e:
        print("Speech Error:", e)


# -----------------------------
# AI PROCESSING
# -----------------------------

def aiProcess(command):

    if not OPENAI_API_KEY:
        return "OpenAI API key is not configured."

    try:
        client = OpenAI(api_key=OPENAI_API_KEY)

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a virtual assistant named Anaya. "
                        "You help with general tasks like Alexa and Google Assistant. "
                        "Give short and simple responses."
                    )
                },
                {
                    "role": "user",
                    "content": command
                }
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        print("OpenAI Error:", e)
        return "Sorry, I could not process that request."


# -----------------------------
# COMMAND PROCESSING
# -----------------------------

def processCommand(command):

    command = command.lower().strip()

    # Open Google
    if "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://google.com")

    # Open Facebook
    elif "open facebook" in command:
        speak("Opening Facebook.")
        webbrowser.open("https://facebook.com")

    # Open YouTube
    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")

    # Open LinkedIn
    elif "open linkedin" in command:
        speak("Opening LinkedIn.")
        webbrowser.open("https://linkedin.com")

    # Play music
    elif command.startswith("play"):

        parts = command.split(" ", 1)

        if len(parts) < 2:
            speak("Please tell me which song to play.")
            return

        song = parts[1].strip()

        if song in musicLibrary.music:
            speak("Playing " + song)
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Sorry, I don't have that song in my music library.")

    # News
    elif "news" in command:

        if not NEWS_API_KEY:
            speak("News API key is not configured.")
            return

        try:
            url = (
                "https://newsapi.org/v2/top-headlines"
                "?country=in"
                "&apiKey=" + NEWS_API_KEY
            )

            response = requests.get(url, timeout=10)

            if response.status_code == 200:

                data = response.json()
                articles = data.get("articles", [])

                if not articles:
                    speak("I couldn't find any news right now.")
                    return

                speak("Here are the latest news headlines.")

                for article in articles[:5]:
                    title = article.get("title")

                    if title:
                        speak(title)

            else:
                print("News API Error:", response.text)
                speak("Sorry, I could not get the news.")

        except Exception as e:
            print("News Error:", e)
            speak("There was a problem getting the news.")

    # Exit
    elif command in ["exit", "quit", "stop", "goodbye"]:

        speak("Goodbye.")
        exit()

    # AI
    else:

        output = aiProcess(command)
        speak(output)


# -----------------------------
# MAIN PROGRAM
# -----------------------------

if __name__ == "__main__":

    speak("Initializing your AI assistant Anaya.")

    recognizer = sr.Recognizer()

    while True:

        print("\nWaiting for wake word 'Anaya'...")

        try:

            # Listen for wake word
            with sr.Microphone() as source:

                recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                print("Listening...")
                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=3
                )

            word = recognizer.recognize_google(audio)

            print("You said:", word)

            # Check wake word
            if word.lower().strip() == "anaya":

                speak("Yes?")

                # Listen for command
                with sr.Microphone() as source:

                    print("Anaya Active...")
                    audio = recognizer.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=8
                    )

                command = recognizer.recognize_google(audio)

                print("Command:", command)

                processCommand(command)

        except sr.WaitTimeoutError:
            print("No speech detected.")

        except sr.UnknownValueError:
            print("Could not understand the audio.")

        except sr.RequestError as e:
            print("Speech recognition service error:", e)

        except Exception as e:
            print("Error:", e)
        
