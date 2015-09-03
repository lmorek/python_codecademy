__author__ = 'morek'

def count(sequence, item):
    found=0
    for n in sequence:
        if n==item:
            found+=1
    return found

seq=[1,2,3,2,3,5,6]

print count(seq, 0)