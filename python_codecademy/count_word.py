__author__ = 'morek'


def fizz_count(x):
    count = 0
    for item in x:
        if item =="fizz":
            count= count +1

    return count

x= ["fizz", "cat", "fizz","dog", "fizz"]
costam=fizz_count(x)
print costam
