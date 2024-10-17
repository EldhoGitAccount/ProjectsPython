def sentence_maker(text):
    wordfilter = ("how", "what", "why")
    capitlized_text = text.capitalize()
    if(text.startswith(wordfilter)):
        return "{}?".format(capitlized_text)
    else:
        return "{}.".format(capitlized_text)

output = []

while True:
    user_input = input("Say something: ")
    if user_input == '\end':
        break
    else:
        output.append(sentence_maker(user_input))

print(" ".join(output))
    

