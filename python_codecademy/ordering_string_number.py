__author__ = 'morek'

def high_and_low(numbers):
    words = numbers.split()
    words = [int(item) for item in words]

    return str(max(words))+" "+str(min(words))
