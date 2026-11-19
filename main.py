import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary as s

# Initialize engine once
engine = pyttsx3.init()
recognizer = sr.Recognizer()

# Text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech to text / 
# Listning for command
def processCommand(command):
    print("Processing command:", command)
    if "google" in command.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "youtube" in command.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "play" in command.lower():
        song = command.lower().split(" ")[1]
        link = s.music[song]
        webbrowser.open(link)
    else:
        speak("Sorry, I don't know that command yet")
    
# This code will run only in this file
if __name__ == "__main__":
    speak("Sir Shoaib Initializing Jarvis please wait for a sec...")

    # First step it will listen Jervis for activation
    while True:
        try:

            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source)
                word = recognizer.recognize_google(audio)
                print("You said:", word)
                
            if word.lower() == "jarvis":
                speak("Yes sir")
                # Second step it will listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active... Listening for command")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    print("Command:", command)
                    processCommand(command)

        except Exception as e:
            print("Sorry, I could not understand your audio:", e)
