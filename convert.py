import math

def fl_addition (eq: list, index: int) -> float:
    return float(eq[index-1]) + float(eq[index+1])

def int_addition(eq: list, index: int) -> int:
    return int(eq[index-1]) + int(eq[index+1])

def int_subtraction(eq: list, index: int) -> int:
    return int(eq[index-1]) - int(eq[index+1])

def int_multiply(eq: list, index: int) -> int:
    return int(eq[index-1]) * int(eq[index+1])

def int_divide(eq: list, index: int) -> int:
    return int(eq[index-1]) / int(eq[index+1])

def int_exp(eq: list, index: int) -> int:
    return math.pow(int(eq[index-1]),int(eq[index+1]))

def int_factorial(eq: list, index: int) -> int:
    return math.factorial(int(eq[index -1]))

def get_math_syntax (text: str) -> str:
    text = text.lower()
    text = text.replace("to the", "^")
    text = text.replace("th power", "")
    text = text.replace("rd power", "")
    text = text.replace("st power", "")
    text = text.replace("squared", "^ 2")
    text = text.replace("cubed", "^ 3")
    text = text.replace("factorial", "!")
    return text

def order_of_operation(eq: list) -> list:
    while len(eq) != 1:
        if "!" in eq:
            x = int_factorial(eq, eq.index("!"))
            del eq[eq.index("!") - 1]
            eq.insert(eq.index("!"), x)
            del eq[eq.index("!")]
        elif "^" in eq:
            x = int_exp(eq, eq.index("^"))
            del eq[eq.index("^") - 1]
            del eq[eq.index("^") + 1]
            eq.insert(eq.index("^"), x)
            del eq[eq.index("^")]
        elif "/" in eq:
            x = int_divide(eq, eq.index("/"))
            del eq[eq.index("/") - 1]
            del eq[eq.index("/") + 1]
            eq.insert(eq.index("/"), x)
            del eq[eq.index("/")]
        elif "*" in eq:
            x = int_multiply(eq, eq.index("*"))
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
            x = int_subtraction(eq, eq.index("-"))
            del eq[eq.index("-") - 1]
            del eq[eq.index("-") + 1]
            eq.insert(eq.index("-"), x)
            del eq[eq.index("-")]
    return eq
