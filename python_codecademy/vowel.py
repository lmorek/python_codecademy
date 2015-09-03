__author__ = 'morek'
def anti_vowel(text):
    temp=""
    list1=['a','A','e','E','i','I','o','O','u','U']
    for letter in text:
        if letter not in list1:
            temp = temp+letter

    return temp


print anti_vowel("hello")