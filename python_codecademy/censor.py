__author__ = 'morek'

def censor(text, word):
    censored = []
    z =text.split(" ")
    for i in z:
        if i in word:
            censored.append(len(word) * '*')
        else:
            censored.append(i)
    x = " ".join(censored)
    return x
