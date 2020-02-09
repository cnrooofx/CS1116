#!/usr/local/bin/python3

from cgi import FieldStorage
from random import randint
from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()
choice = form_data.getfirst('rsp', '')

rsp_dict = {0: 'Rock', 1: 'Scissors', 2: 'Paper'}
outcome = ''

try:
    user = int(choice)
    if user in rsp_dict:
        user_out = rsp_dict[user]
        computer = randint(0, 2)
        comp_out = rsp_dict[computer]
        if computer == user:
            outcome = 'Computer\'s %s ties with User\'s %s' % (comp_out, user_out)
        elif (user + 1) % 3 == computer:
            outcome = 'User\'s %s beats Computer\'s %s' % (user_out, comp_out)
        else:
            outcome = 'Computer\'s %s beats User\'s %s' % (comp_out, user_out)
    else:
        outcome = 'Error! Incorrect number'
except ValueError:
    outcome = 'Error! Please enter a number'

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <link rel="stylesheet" href="lengths.css" />
            <title>Lengths</title>
        </head>
        <body>
            <p>
                %s
            </p>
        </body>
    </html>""" % (outcome))
