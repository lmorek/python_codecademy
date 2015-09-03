__author__ = 'morek'

char=raw_input("Enter here some word: ")
def reverse(text):
    x = []
    y = len(text) - 1
    while y >= 0:
        for letter in text[y]:
            x.append(letter)
            y -= 1

    return "".join(x)

print reverse(char)