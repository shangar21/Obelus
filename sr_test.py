
import speech_recognition as sr

def int_addition(text: str) -> int:
    index = text.find("+")
    x = int(text[:index - 1])
    y = int(text[index + 2:])
    return x + y


def int_subtraction(text: str) -> int:
    index = text.find("-")
    x = int(text[:index - 1])
    y = int(text[index + 2:])
    return x - y



def int_multiply(text: str) -> int:
    index = text.find("*")
    x = int(text[:index - 1])
    y = int(text[index + 2:])
    return x * y


def int_devide(text: str) -> int:
    index = text.find("\\")
    x = int(text[:index - 1])
    y = int(text[index + 2:])
    return (x//y)


r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something : ")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(text)
        print(int_subtraction(text))

    except:
        print("Sorry, unable to understand.")

#print(int_multiply(text))

#print(int_addition(text))

#print(int_subtraction(text))

