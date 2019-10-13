
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something : ")
    audio = r.listen(source)

    try:
       text = r.recognize_google(audio)
       print(text)
       index = text.find("+")
       print(int(text[: index - 1]) + int(text[index + 2:]))

    except:
        print("Sorry, unable to understand.")
