'''
DOCSTRING: Function that takes arbitary number of arguments and returns list of even numbers
IN       : numbers, eg:18,4,6,5
OUTPUT   : [18,4,6]
'''
def even_list(*args):
    myList = [num for num in args if num%2 == 0]
    return myList
    
even_list = even_list(2,6,7,4,3)
print('Even list of arguments is {}'.format(even_list))