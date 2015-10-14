
__author__ = 'morek'

numbers = "1 -2 3 4 5 6 7 8"
def high_and_low(numbers):
    words = numbers.split()
    words = [int(item) for item in words]

    lista= [max(words),  min(words)]

    return lista

print high_and_low(numbers)