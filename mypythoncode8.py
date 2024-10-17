output = ''

while True:
    text = input("Say something: ")
    if text == '\end':
        break
    else:
        if( text.find("how") != -1):
            text = text.capitalize() + '?'
        else:
            text = text.capitalize() + '.'

        output = output + text
        continue

print(output)
    

