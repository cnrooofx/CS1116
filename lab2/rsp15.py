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
beats_dict = {0: {1: "pounds out", 2: "crushes", 3: "crushes", 4: "crushes", 5: "blocks", 6: "crushes", 7: "crushes"},
              1: {2: "melts", 3: "burns", 4: "burns", 5: "burns", 6: "burns", 7: "burns", 8: "burns"},
              2: {3: "cut", 4: "cut", 5: "carve", 6: "cut", 7: "cut", 8: "cut", 9: "swish through"},
              3: {4: "bites", 5: "nests in", 6: "bites", 7: "swallows", 8: "nests in", 9: "breathes", 10: "drinks"},
              4: {5: "plants", 6: "tames", 7: "cleans with", 8: "writes", 9: "breathes", 10: "drinks", 11: "slays"},
              5: {6: "shelters", 7: "outlives", 8: "becomes", 9: "produces", 10: "drinks", 11: "shelters", 12: "imprisons"},
              6: {7: "chews up", 8: "chews up", 9: "breathes", 10: "drinks", 11: "outruns", 12: "bites", 13: "outruns"},
              7: {8: "soaks", 9: "uses", 10: "absorbs", 11: "cleanses", 12: "cleanses", 13: "conducts", 14: "cleans"},
              8: {9: "fans", 10: "floats on", 11: "rebukes", 12: "rebukes", 13: "defines", 14: "outlaws", 0: "covers"},
              9: {10: "evaporates", 11: "freezes", 12: "chokes", 13: "creates", 14: "tarnishes", 0: "erodes", 1: "blows out"},
              10: {11: "drowns", 12: "drowns", 13: "conducts", 14: "rusts", 0: "erodes", 1: "puts out", 2: "rusts"},
              11: {12: "commands", 13: "breathes", 14: "immune to", 0: "rests on", 1: "breathes", 2: "immune to", 3: "spawns"},
              12: {13: "casts", 14: "immune to", 0: "hurls", 1: "breathes", 2: "immune to", 3: "eats", 4: "possesses"},
              13: {14: "melts", 0: "splits", 1: "starts", 2: "melts", 3: "strikes", 4: "strikes", 5: "splits"},
              14: {0: "targets", 1: "fires", 2: "outclasses", 3: "shoots", 4: "shoots", 5: "targets", 6: "shoots"}}
extras_dict = {6: {12: "\'s heiney"}, 7: {9: " pockets"}}

outcome = ''
extras = ''

try:
    user = int(choice)
    if user in rsp_dict:
        user_out = rsp_dict[user]
        computer = randint(0, 14)
        comp_out = rsp_dict[computer]
        if computer == user:
            outcome = 'Computer\'s %s ties with User\'s %s' % (comp_out, user_out)
        elif ((user - computer) % 15) > 7:
            if (user == 6 and computer == 12) or (user == 7 and computer == 9):
                extras = extras_dict[user][computer]
            outcome = 'User\'s %s %s Computer\'s %s%s' % (user_out, beats_dict[user][computer], comp_out, extras)
        else:
            if (computer == 6 and user == 12) or (computer == 7 and user == 9):
                extras = extras_dict[computer][user]
            outcome = 'Computer\'s %s %s User\'s %s%s' % (comp_out, beats_dict[computer][user], user_out, extras)
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
            <title>Result</title>
        </head>
        <body>
            <p>
                %s
            </p>
        </body>
    </html>""" % (outcome))
