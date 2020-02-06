#!/usr/local/bin/python3

from cgi import FieldStorage
from random import randint
from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()
choice = form_data.getfirst('rsp', '')

rsp_dict = {0: 'Rock', 1: 'Fire', 2: 'Scissors', 3: 'Snake', 4: 'Human',
            5: 'Tree', 6: 'Wolf', 7: 'Sponge', 8: 'Paper', 9: 'Air',
            10: 'Water', 11: 'Dragon', 12: 'Devil', 13: 'Lightning',
            14: 'Gun'}
outcome = ''

try:
    # user = int(choice)
    user = 4
    if user in rsp_dict:
        user_out = rsp_dict[user]
        computer = randint(0, 15)
        comp_out = rsp_dict[computer]
        if computer == user:
            outcome = 'Computer\'s %s ties with User\'s %s' % (comp_out, user_out)
        elif (user + 7) % 15 >= computer:
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
