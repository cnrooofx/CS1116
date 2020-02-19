#!/usr/local/bin/python3

from cgi import FieldStorage
from random import randint
import ast
from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()
choice1 = form_data.getfirst('rsp1', '')
choice2 = form_data.getfirst('rsp2', '')

rsp_dict = {0: 'dynamite', 1: 'tornado', 2: 'quicksand', 3: 'pit', 4: 'chain',
            5: 'gun', 6: 'law', 7: 'whip', 8: 'sword', 9: 'rock', 10: 'death',
            11: 'wall', 12: 'sun', 13: 'camera', 14: 'fire', 15: 'chainsaw',
            16: 'school', 17: 'scissors', 18: 'poison', 19: 'cage', 20: 'axe',
            21: 'peace', 22: 'computer', 23: 'castle', 24: 'snake',
            25: 'blood', 26: 'porcupine', 27: 'vulture', 28: 'monkey',
            29: 'king', 30: 'queen', 31: 'prince', 32: 'princess',
            33: 'police', 34: 'woman', 35: 'baby', 36: 'man', 37: 'home',
            38: 'train', 39: 'car', 40: 'noise', 41: 'bicycle', 42: 'tree',
            43: 'turnip', 44: 'duck', 45: 'wolf', 46: 'cat', 47: 'bird',
            48: 'fish', 49: 'spider', 50: 'cockroach', 51: 'brain',
            52: 'community', 53: 'cross', 54: 'money', 55: 'vampire',
            56: 'sponge', 57: 'church', 58: 'butter', 59: 'book', 60: 'paper',
            61: 'cloud', 62: 'aeroplane', 63: 'moon', 64: 'grass', 65: 'film',
            66: 'toilet', 67: 'air', 68: 'planet', 69: 'guitar', 70: 'bowl',
            71: 'cup', 72: 'beer', 73: 'rain', 74: 'water', 75: 'T.V.',
            76: 'rainbow', 77: 'U.F.O.', 78: 'alien', 79: 'prayer',
            80: 'mountain', 81: 'satan', 82: 'dragon', 83: 'diamond',
            84: 'platinum', 85: 'gold', 86: 'devil', 87: 'fence',
            88: 'video game', 89: 'maths', 90: 'robot', 91: 'heart',
            92: 'electricity', 93: 'lightning', 94: 'medusa', 95: 'power',
            96: 'laser', 97: 'nuke', 98: 'sky', 99: 'tank', 100: 'helicopter'}

gifs = [18, 35, 39, 48, 54, 75, 84, 85, 88, 90]

file = open('dictionary.txt', 'r')
beats_dict = ast.literal_eval(file.read())

outcome = ''
extras = ''

try:
    player1 = int(choice1)
    if choice2 != '':
        player2 = int(choice2)
        name1 = 'Player 1'
        name2 = 'Player 2'
    else:
        player2 = randint(0, 100)
        name1 = 'Player'
        name2 = 'Computer'
    if player1 in rsp_dict and player2 in rsp_dict:
        player1_out = rsp_dict[player1]
        player2_out = rsp_dict[player2]
        if player2 == player1:
            heading = 'It\'s a tie'
            if player1 in gifs:
                outcome += '<figure><img src="img/%s.gif" alt="%s"  /></figure>' % (player1, player1_out)
            else:
                outcome += '<figure><img src="img/%s.png" alt="%s"  /></figure>' % (player1, player1_out)
            outcome += '<p>%s\'s %s ties with %s\'s %s</p>' % (name1, player1_out, name2, player2_out)
        elif ((player1 - player2) % 101) > 50:
            heading = '%s Wins!' % (name1)
            if player1 in gifs:
                outcome += '<figure><img src="img/%s.gif" alt="%s"  />' % (player1, player1_out)
            else:
                outcome += '<figure><img src="img/%s.png" alt="%s"  />' % (player1, player1_out)
            if player2 in gifs:
                outcome += '<img src="img/%s.gif" alt="%s"  /></figure>' % (player2, player2_out)
            else:
                outcome += '<img src="img/%s.png" alt="%s"  /></figure>' % (player2, player2_out)
            outcome += '<p>%s %s%s%s</p>' % (player1_out.capitalize(), beats_dict[player1][player2][0], player2_out, beats_dict[player1][player2][1])
        else:
            heading = '%s Wins!' % (name2)
            if player2 in gifs:
                outcome += '<figure><img src="img/%s.gif" alt="%s" />' % (player2, player2_out)
            else:
                outcome += '<figure><img src="img/%s.png" alt="%s" />' % (player2, player2_out)
            if player1 in gifs:
                outcome += '<img src="img/%s.gif" alt="%s" /></figure>' % (player1, player1_out)
            else:
                outcome += '<img src="img/%s.png" alt="%s" /></figure>' % (player1, player1_out)
            outcome += '<p>%s %s%s%s</p>' % (player2_out.capitalize(), beats_dict[player2][player1][0], player1_out, beats_dict[player2][player1][1])
    else:
        heading = 'Oops'
        outcome = '</p><strong>Error! Incorrect number</strong></p>'
except ValueError:
    heading = 'Oops'
    outcome = '<p>Please choose a weapon</p>'

file.close()

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
                    Rock Scissors Paper 101
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
