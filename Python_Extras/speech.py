import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening......")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"User said : {text}")
    except:
        print("Sorry, what you said was not understood. Please repeat")
