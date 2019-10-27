import speech_recognition as sr
import convert

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something : ")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        text = convert.get_math_syntax(text)
        print(text)
        arr = text.split(" ")
        #print(*arr, sep=",")
        word = convert.seperate_cf(arr[5])
        arr[5] = "x"
        arr.insert(5, word)
        print(*arr, sep=",")
        #arr = convert.replace_digits(arr)
        arr = convert.quadratic(arr)
        '''
        if "log" in arr:
            arr = convert.logarithm(arr)
        elif "sine" in arr:
            arr = convert.trigno(arr)
        else:
            arr = convert.order_of_operation(arr)
        
        '''
        print(*arr)
    except:
        print("Sorry, unable to understand.")



#print(int_multiply(text))

#print(int_addition(text))

#print(int_subtraction(text))

