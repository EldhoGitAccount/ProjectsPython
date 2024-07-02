import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # search digit numeric character of the format specified
print(phoneNumRegex.findall('Call me tomorrow, at 445-556-6767 or in my other number 455-667-5666'))
