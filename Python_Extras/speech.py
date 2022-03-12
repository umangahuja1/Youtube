import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening.......")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("User's  input : {}".format(text))
    except:
        print("Sorry, the input given was not recognised. Please try again :) ")
