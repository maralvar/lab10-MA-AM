# https://github.com/maralvar/lab10-MA-AM.git
# Partner 1: Mario A Alvarez
# Partner 2: Atreyu Morales

"""
calculator.py
Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        return math.sqrt(a)
    except:
        raise ValueError

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except:
        raise ValueError

def add(a, b):

    result = a + b
    return result

def mul(a, b):

    result = a * b
    return result

def div(a, b):

    if a == 0:

        raise ZeroDivisionError

    result = b / a # raise ZeroDivisionError if a == 0
    return result

def subtract(a, b):
    return a - b

def logarithm(a, b):
    try:
        return math.log(b, a) # use math library/raise ValueError
    except:
        raise ValueError

def exp(a, b):

    result = pow(a, b)
    return result