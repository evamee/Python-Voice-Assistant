import speech_recognition as sr
import pyttsx3
import pywhatkit


engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def startup(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    hear_me = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = hear_me.listen(source)
            audio = hear_me.recognize_google(voice)
            audio = audio.lower()
            print(audio)
    except :
        pass
    return audio


def run_alexa():
    command = take_command()
    
    if "play" in command:
        song = command.replace("play"," ")
        startup(f"playing {song}")
        pywhatkit.playonyt(song)



startup("i am alexa what can i do for you?")
run_alexa()










