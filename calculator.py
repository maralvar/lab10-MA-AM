"""
calculator.py
Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):

    result = a + b
    return result

def sub(a, b):

    result = a - b
    return result

def mul(a, b):

    result = a * b
    return result

def div(a, b):

    if a == 0:

        raise ZeroDivisionError

    result = b / a # raise ZeroDivisionError if a == 0
    return result

def log(a, b):


    try:
        result = math.log(a, b)# use math library + raise ValueError
    except:

       raise ValueError

    return result

def exp(a, b):

    result = pow(a, b)
    return result