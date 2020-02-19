#!/usr/local/bin/python3

from cgi import FieldStorage
from random import randint
from html import escape
from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()
choice1 = escape(form_data.getfirst('rsp1', '').strip())
choice2 = escape(form_data.getfirst('rsp2', '').strip())
name1 = escape(form_data.getfirst('name1', 'Player 1').strip())
name2 = escape(form_data.getfirst('name2', 'Player 2').strip())

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
    player1 = int(choice1)
    if choice2 == '':
        player2 = randint(0, 14)
        if name1 == 'Player 1':
            name1 = 'Player'
        name2 = 'Computer'

    else:
        player2 = int(choice2)
    if player1 in rsp_dict and player2 in rsp_dict:
        player1_out = rsp_dict[player1]
        player2_out = rsp_dict[player2]
        if player2 == player1:
            heading = 'It\'s a tie'
            outcome += '<figure><img src="img15/%s.png" alt="%s"  /></figure>' % (player1, player1_out)
            outcome += '<p>%s\'s %s ties with %s\'s %s</p>' % (name2, player2_out, name1, player1_out)
        elif ((player1 - player2) % 15) > 7:
            if (player1 == 6 and player2 == 12) or (player1 == 7 and player2 == 9):
                extras = extras_dict[player1][player2]
            heading = '%s Wins!' % (name1)
            outcome += '<figure><img src="img15/%s.png" alt="%s"  />' % (player1, player1_out)
            outcome += '<img src="img15/%s.png" alt="%s"  /></figure>' % (player2, player2_out)
            outcome += '<p>%s\'s %s %s %s\'s %s%s</p>' % (name1, player1_out, beats_dict[player1][player2], name2, player2_out, extras)
        else:
            if (player2 == 6 and player1 == 12) or (player2 == 7 and player1 == 9):
                extras = extras_dict[player2][player1]
            heading = '%s Wins!' % (name2)
            outcome += '<figure><img src="img15/%s.png" alt="%s"  />' % (player2, player2_out)
            outcome += '<img src="img15/%s.png" alt="%s"  /></figure>' % (player1, player1_out)
            outcome += '<p>%s\'s %s %s %s\'s %s%s</p>' % (name2, player2_out, beats_dict[player2][player1], name1, player1_out, extras)
    else:
        heading = 'Oops'
        outcome = '<strong>Error! Incorrect number</strong>'
except ValueError:
    heading = 'Oops'
    outcome = '<strong>Error! Please enter a number</strong>'

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <link rel="stylesheet" href="rsp.css" />
            <title>RSP | Result</title>
        </head>
        <body>
            <header>
                <h1>
                    Rock Scissors Paper 15
                </h1>
            </header>
            <main>
                <h2>
                    %s
                </h2>
                %s
                <p class="again">
                    <a href="https://cs1.ucc.ie/~cf26/game.html">Click here to play again</a>
                </p>
            </main>
        </body>
    </html>""" % (heading, outcome))
