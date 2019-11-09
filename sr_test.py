import speech_recognition as sr
import convert

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something : ")
    audio = r.listen(source)

    #lst = ["21", "x", "^", "2", "-", "x", "-", "30", "+","x", "^", "4", "+", "9", "x", "^", "3"]

    #print(*convert.poly(lst))


    try:
        text = r.recognize_google(audio)
        text = convert.get_math_syntax(text)
        arr = text.split(" ")
        print(*arr, sep = ",")

        if "solve" in arr[0]:
            arr = arr[1:]
            for i in range(len(arr)):
                if "x" in arr[i]:
                    if arr[i][0].isdigit():
                        string = convert.seperate_cf(arr[i])
                        if string != None:
                            arr[i] = "x"
                            arr.insert(i, string)
            print(*convert.poly(arr))
        elif arr[0] in ["sine", "cos", "tan", "arcsine", "arccos", "arctan"]:
            arr = convert.trigno(arr)
            print(*arr)
        elif "log" in arr[0]:
            arr = convert.logarithm(arr)
            print(*arr)
    except:
        print("Sorry, unable to understand.")


#print(int_multiply(text))

#print(int_addition(text))

#print(int_subtraction(text))

