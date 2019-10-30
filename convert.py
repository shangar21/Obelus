import math
import numpy

def fl_addition (eq: list, index: int) -> float:
    return float(eq[index-1]) + float(eq[index+1])

def fl_subtraction(eq: list, index: int) -> float:
    return float(eq[index-1]) - float(eq[index+1])

def fl_multiply(eq: list, index: int) -> float:
    return float(eq[index - 1]) * float(eq[index + 1])

def fl_divide(eq: list, index: int) -> float:
    return float(eq[index-1]) / float(eq[index+1])

def fl_exp(eq: list, index: int) -> float:
    return math.pow(float(eq[index-1]),float(eq[index+1]))

def int_factorial(eq: list, index: int) -> int:
    return math.factorial(int(eq[index -1]))

def replace_digits(eq: list) -> list:
    for i in eq:
        if i.isdigit():
            eq[eq.index(i)] = float(i)
    return eq

def get_math_syntax (text: str) -> str:
    text = text.lower()
    text = text.replace("to the", "^")
    text = text.replace("th power", "")
    text = text.replace("rd power", "")
    text = text.replace("st power", "")
    text = text.replace("squared", "^ 2")
    text = text.replace("cubed", "^ 3")
    text = text.replace("factorial", "!")
    text = text.replace("times", "*")
    text = text.replace("sine of", "sine")
    text = text.replace("sign", "sine")
    text = text.replace("cosine", "cos")
    text = text.replace("cosine of", "cos")
    text = text.replace("tangent", "tan")
    text = text.replace("tangent of", "tan")
    text = text.replace("sine inverse", "arcsin")
    text = text.replace("cos inverse", "arccos")
    text = text.replace("plus", "+")
    text = text.replace("log of", "log")
    text = text.replace("minus", "-")
    return text

def order_of_operation(eq: list) -> list:
    while len(eq) != 1:
        if "!" in eq:
            x = int_factorial(eq, eq.index("!"))
            del eq[eq.index("!") - 1]
            eq.insert(eq.index("!"), x)
            del eq[eq.index("!")]
        elif "^" in eq:
            x = fl_exp(eq, eq.index("^"))
            del eq[eq.index("^") - 1]
            del eq[eq.index("^") + 1]
            eq.insert(eq.index("^"), x)
            del eq[eq.index("^")]
        elif "/" in eq:
            x = fl_divide(eq, eq.index("/"))
            del eq[eq.index("/") - 1]
            del eq[eq.index("/") + 1]
            eq.insert(eq.index("/"), x)
            del eq[eq.index("/")]
        elif "*" in eq:
            x = fl_multiply(eq, eq.index("*"))
            del eq[eq.index("*") - 1]
            del eq[eq.index("*") + 1]
            eq.insert(eq.index("*"), x)
            del eq[eq.index("*")]
        elif "+" in eq:
            x = fl_addition(eq, eq.index("+"))
            del eq[eq.index("+") - 1]
            del eq[eq.index("+") + 1]
            eq.insert(eq.index("+"), x)
            del eq[eq.index("+")]
        else:
            x = fl_subtraction(eq, eq.index("-"))
            del eq[eq.index("-") - 1]
            del eq[eq.index("-") + 1]
            eq.insert(eq.index("-"), x)
            del eq[eq.index("-")]
    return eq

def trigno (eq: list) -> list:
    if "sine" in eq:
        arr = eq[eq.index("sine") + 1: ]
        arr = order_of_operation(arr)
        x = round(math.sin(arr[0]), 8)
        eq.clear()
        eq.append(x)
    elif "cos" in eq:
        arr = eq[eq.index("sine") + 1: ]
        arr = order_of_operation(arr)
        x = round(math.cos(arr[0]), 8)
        eq.clear()
        eq.append(x)
    elif "tan" in eq:
        arr = eq[eq.index("sine") + 1: ]
        arr = order_of_operation(arr)
        x = round(math.tan(arr[0]), 8)
        eq.clear()
        eq.append(x)
    elif "arcsin" in eq:
        arr = eq[eq.index("arcsin") + 1:]
        arr = order_of_operation(arr)
        x = round(math.asin(arr[0]), 8)
        eq.clear()
        eq.append(x)
    elif "arccos" in eq:
        arr = eq[eq.index("arccos") + 1:]
        arr = order_of_operation(arr)
        x = round(math.acos(arr[0]), 8)
        eq.clear()
        eq.append(x)
    elif "arctan" in eq:
        arr = eq[eq.index("arctan") + 1: ]
        arr = order_of_operation(arr)
        x = round(math.atan(arr[0]), 8)
        eq.clear()
        eq.append(x)
    return eq

def logarithm (eq: list) -> list:
    if "/" in  eq:
        if eq[eq.index("/") + 1] == "log":
            arr1 = eq[eq.index("log") + 1: eq.index("/")]
            arr1 = order_of_operation(arr1)
            arr2 = eq[eq.index("/") + 2:]
            arr2 = order_of_operation(arr2)
            eq.clear()
            eq.append(math.log(arr1[0],10)/math.log(arr2[0], 10))
    else:
        arr = eq[eq.index("log") + 1: ]
        arr = order_of_operation(arr)
        eq.clear()
        eq.append(math.log(arr[0],10))
    return eq

def poly(eq: list) -> list:
    powers = []
    coefficients = []

    for i in range(len(eq)):
        if eq[i] == "-":
            num = eq[i] + eq[i + 1]
            eq[i] = "+"
            eq.pop(i+1)
            eq.insert(i + 1, num)
    for i in range(len(eq)):
        if eq[i] == "^":
            if i - 1 < 0 or not eq[i - 2].isdigit():
                coefficients.append(1.0)
            else:
                powers.append(eq[i + 1])
                coefficients.append(eq[i - 2])
    eqn = zip(powers, coefficients)
    eqn = sorted(eqn)
    powers, coefficients = list(eqn)
    eq = numpy.roots(coefficients)
    eq = list(eq)

    return eq

def seperate_cf(eq: list):
    num = ''
    for i in eq:
        if "x" in i:
            for j in i:
                if j.isdigit():
                    num += j
            eq[eq.index(i)] = "x"
            eq.insert(eq.index(i), num)
    for i in eq:
        if i.isdigit:
            eq[eq.index(i)] = float(i)