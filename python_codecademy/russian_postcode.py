__author__ = 'morek'

def zipvalidate(postcode):

         if len(postcode)==6 and postcode[0] not in "05789" and postcode.isdigit():
                 return True
         else:
                 return False
print zipvalidate("nd3ur9382rj")