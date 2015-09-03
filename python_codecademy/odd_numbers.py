__author__ = 'morek'
def purify(lis):
    lis2 = []
    for num in lis:
        if num % 2 == 0:
            lis2.append(num)
    return lis2

lista=[1,2,3,4,5,6,7]
print purify(lista)