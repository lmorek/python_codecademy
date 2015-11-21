__author__ = 'lukasz'

import random
from random import randrange

LST = ["1","2","3","4","5"]



nowa_lista=""

while LST !=[]:
    #print("item:", item)
    word=random.choice(LST)
    #print("1:", word)
    if word not in nowa_lista:
        nowa_lista+=(word+" ")
        LST.remove(word)
    elif word in nowa_lista:
        print("to jzu było")

print(nowa_lista + " ")



#while word not in nowa_lista:
#for item in range(len(LST)):
  #  if word not in nowa_lista:

        #print(nowa_lista)











# wybieram random.choice i wstawiam do nowej listy
# wywoluje kolejny raz random.choice, sprawdzam czy dane slowo zostało uzyte,
# jak tak to nie wpisuje go do nowej listy,