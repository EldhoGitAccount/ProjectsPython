mynums = [1,2,3,4,5,6]
mynames = ['Andy', 'Eva', 'John']

# squaring applied to all numbers in list
print(list(map(lambda num: num ** 2, mynums)))
# filtering out even numbers
print(list(filter(lambda num: num%2 == 0, mynums)))
# reversing all names in the list
print(list(map(lambda x: x[::-1] , mynames)))