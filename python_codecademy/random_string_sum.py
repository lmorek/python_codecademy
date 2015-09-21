__author__ = 'morek'
def random_string_sum(random_word):
    lst=0
    for item in random_word:
        if item in "0123456789":
            lst=lst+int(item)
    print lst






z= random_string_sum("som4e rando2m 12a3")

print z
