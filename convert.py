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

def fl_sine(eq: list, index: int) -> float:
    return math.sin(float(eq[index + 1]))

def fl_cosine(eq: list, index: int) -> float:
    return math.cos(float(eq[index + 1]))

def fl_tangent(eq: list, index: int) -> float:
    return math.tan(float(eq[index + 1]))

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
    return text

def order_of_operation(eq: list) -> list:
    while len(eq) != 1:
        if "sine" in eq:
            x = fl_sine(eq, eq.index("sine"))
            del eq[eq.index("sine") + 1]
            eq.insert(eq.index("sine"), x)
            del eq[eq.index("sine")]
        elif "!" in eq:
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
