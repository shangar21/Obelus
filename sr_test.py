import speech_recognition as sr
import convert

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something : ")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        text = convert.get_math_syntax(text)
        arr = text.split(" ")
        arr = convert.seperate_cf(arr)
        print(*arr)
        print(*convert.poly(arr))
    except:
        print("Sorry, unable to understand.")



#print(int_multiply(text))

#print(int_addition(text))

#print(int_subtraction(text))

