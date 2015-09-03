__author__ = 'morek'

def factorial(x):
    fact = 1
    while x > 0:
        fact *= x
        x -= 1
    return fact