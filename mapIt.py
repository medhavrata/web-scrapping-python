#!/home/gitpod/.pyenv/shims/python

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    #get address from command line
    address = ' '.join(sys.argv[1:])
else:
    #get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

webbrowser.open('https://www.next.co.uk/')