__author__ = 'morek'
def count_by(x,y):
    item=1
    lst=[]

    for item in range(y+1):

        multiply=item*x
        if multiply >0:

            lst.append(multiply)
    print lst




print count_by(2,5)
