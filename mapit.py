import webbrowser, sys, pyperclip
sys.argv #['mapit.py', '870', 'Valecia', 'st']

#check if command line arguments are passed
if len(sys.argv) > 1 :
    address = ' '.join(sys.argv[1:])
else :
    address = pyperclip.paste()

#https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)
