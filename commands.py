import speech_recognition as sr
import webbrowser
from commands import *
import pyttsx3 as tts
from datetime import datetime
from playsound import playsound
import ctypes

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)

    try:
        aud = r.recognize_google(audio_text).lower()
        words = aud.split()
        sentence = ''.join(words).lower()

        return [aud, words, sentence]
    
    except:
        return None

def speak(t):
    e = tts.init()
    e.say(t)
    e.runAndWait()
    e.stop()

def time():
    current_time = datetime.now().strftime("TheTimeIs %H %M")
    speak(current_time.split())

def website():
    speak("What website would you like to visit?")
    a = listen()
    if listen == None:
        speak("Did you recognize website")
        return
    webbrowser.open('http://{0}'.format(a[2]))

def youtube():
    webbrowser.open('http://youtube.com')

def twitter():
    webbrowser.open("https://twitter.com")

def instagram():
    webbrowser.open("https://instagram.com")

def overflow():
    webbrowser.open("https://stackoverflow.com")

def roblox():
    webbrowser.open("https://roblox.com")

def close():
    speak("Are you sure?")
    a = listen()
    if a == None or not "yes" in a[1]:
        return
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    hwnd = user32.GetForegroundWindow()
    if hwnd:
        user32.PostMessageA(hwnd, 0x0010, 0, 0)