import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyttsx3


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)



def get_audio():
    hear_me = sr.Recognizer()
    try:
        with sr.Microphone as source:
            print("listening...")
            voice = hear_me.listen(source)
            audio = hear_me.recognize_google(voice)
            print("audio")
    except:
        pass



speak("hello Eyram")
get_audio()

