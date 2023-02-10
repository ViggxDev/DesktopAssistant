import speech_recognition as sr
from commands import *
import webbrowser

r = sr.Recognizer()

forbidden_commands = ["listen", "speak"]

while True:
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
    try:
        aud = r.recognize_google(audio_text).lower()
        words = aud.split()
        sentence = ''.join(words).lower()

        if "quit" in words and "assistant" in words:
            speak("Shutting down!")
            break
        try:
            for x in words:
                try:
                    if not x in forbidden_commands and "assistant" in words:
                        eval(x.lower()+"()")
                        break
                except:
                    Warning("Current word is not a command")
        except:
            print("Did not recognize your command")
    except:
        print("Sorry, I did not get that")