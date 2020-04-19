'''
DOCSTRING: Function for getting back pig latin word
INOUT: string, Eg:word,apple
OUTPUT: ordway, appleay
'''

def pig_latin(word):
        first_letter = word[0]
        if first_letter in 'aeiou':
           pig_word = word + 'ay'
        else:
           pig_word = word[1:] + first_letter + 'ay'
           
        return pig_word
        
pig_latin_string = pig_latin('word')
#pig_latin_string = pig_latin('apple')
print(f'Pig latin for the given string is {pig_latin_string}')
        
           