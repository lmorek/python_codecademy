__author__ = 'morek'

def add_length(str_):
    # counts length of word in a string and adds it to an end of that word
    text =str_.split()
    print text
    lst =[]
    for word in text:
        l=len(word)

        lst+=[ word + " " + str(l)]
    return lst


def string_shuffle(str_):
    # changes order of  first name with a last name,
    lst=str_.split()
    str=' ' .join(lst[::-1])
    return str
add_length("you will win")
string_shuffle("Lukasz Morek")