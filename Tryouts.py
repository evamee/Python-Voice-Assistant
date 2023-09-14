import speech_recognition as sr

listener = sr.Recognizer()

try:
	with sr.Microphone as source:
		print('listening...')
		voice = listener.listen(source)
		audio = listener.recognize_google(voice)
		print(audio)

except Exception as e:
	pass
     