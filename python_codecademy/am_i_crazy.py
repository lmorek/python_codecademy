__author__ = 'morek'
import random
def am_I_afraid(day,num):
    if day == "Monday" and num == 12:
        return True
    elif day == "Tuesday"  and num > 95:
        return True
    elif day == "Wednesday" and num ==34:
        return True
    elif day == "Thursday" and num ==0:
        return True
    elif day == "Friday" and num %2 ==0:
        return True
    elif day =="Saturday" and num == 56:
        return True
    elif day == "Sunday" and num in [-666, 666]:
        return True
    else:
        return False

print am_I_afraid("Friday", 5)


lst= [1,3,4,2,6,7,8,3,5]
lst1 = lst.sort()
print sorted(lst)[-2:]
