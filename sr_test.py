import speech_recognition as sr
import convert
import math

def to_list(string: str) -> list:
    arr2 = []
    for i in string:
        arr2.append(i)
    return arr2

r = sr.Recognizer()


with sr.Microphone() as source:
    print("Say Something : ")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        text = convert.get_math_syntax(text)
        print(text)
        arr = text.split(" ")
        print(*arr, sep=",")
        arr = convert.replace_digits(arr)
        arr = convert.trigno(arr)
        print(*arr)
    except:
        print("Sorry, unable to understand.")



#print(int_multiply(text))

#print(int_addition(text))

#print(int_subtraction(text))

