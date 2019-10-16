def int_addition(eq: list, index: int) -> int:
    return int(eq[index-1]) + int(eq[index+1])


def int_subtraction(eq: list, index: int) -> int:
    return int(eq[index-1]) - int(eq[index+1])



def int_multiply(eq: list, index: int) -> int:
    return int(eq[index-1]) * int(eq[index+1])


def int_divide(eq: list, index: int) -> int:
    return int(eq[index-1]) / int(eq[index+1])

def get_math_syntax (text: str) -> str:
    text.lower()
    text.replace("to the power of", "^")
    text.replace("squared", "^ 2")
    text.replace("cubed", "^ 3")
    if "to the" in text:
        #if text[text.find("to the") + 1]
        pass




def order_of_operation(eq: list) -> list:
    while len(eq) != 1:
        if "/" in eq:
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
            x = int_addition(eq, eq.index("+"))
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
