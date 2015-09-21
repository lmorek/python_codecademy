__author__ = 'morek'
def filter_string(string):
    temp=""
    list=["1","2","3","4","5","6","7","8","9","0"]
    for number in string:
        if number  in list:
            temp=temp+number
    return temp

print filter_string("l345asdasdfa")
