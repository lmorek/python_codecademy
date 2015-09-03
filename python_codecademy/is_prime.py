__author__ = 'morek'
def is_prime(x):

    if x < 2:
        return False
    elif x == 2:
        return True
        print "it is prime number"
    else:
        for n in range(2, x - 1):
            if (x % n) == 0:
                return False
        return True

is_prime(2)