# add two numbers 
def add(a : int ,b : int) -> str:
    return a + b
def subtract(a : int ,b : int) -> str:
    return a - b
def multiply(a : int ,b : int) -> str:
    return a * b
def divide(a : int , b :int)-> str:
    if b == 0:
        raise ValueError ("Division by zero is not allowed")
    return a / b
