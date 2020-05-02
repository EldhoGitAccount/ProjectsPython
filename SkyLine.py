'''
DOCSTRING: Function that takes a string and returns even number of letters as upper case
           and odd number of letters as lower case
IN       : ELDHO
OUTPUT   : eLdHo
'''
def myfunc(string):
    index = 0
    word = ""
    for letter in string:
        if(index%2 == 0):
           word = word + letter.lower()
           index+=1
        else:
           word = word + letter.upper()  
           index+=1
           
    return word
    
myString = myfunc('ELDHO')
print('Entered string output is {}'.format(myString))
