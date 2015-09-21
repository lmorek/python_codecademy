__author__ = 'morek'

def is_pronic(n):

    for item in range(n):
        pronic=item*(item+1)
    return pronic

print is_pronic(3)