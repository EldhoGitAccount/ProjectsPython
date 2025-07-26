import pprint
import pandas

message = 'it was a bright day in June'

count = {}

for character in message :
    count.setdefault(character,0)
    count[character] = count[character] + 1



pprint.pprint(count)
