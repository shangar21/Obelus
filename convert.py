import math

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

def trigno (eq: list):
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
