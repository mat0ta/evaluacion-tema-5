def suma(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "TypeError: a y b necesitan ser números"
    return a + b

def resta(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "TypeError: a y b necesitan ser números"
    return a - b

def multiplicacion(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "TypeError: a y b necesitan ser números"
    return a * b

def division(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "TypeError: a y b necesitan ser números"
    if b == 0:
        return "ZeroDivisionError: b no puede ser 0"
    return a / b