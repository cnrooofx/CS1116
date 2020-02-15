#!/usr/local/bin/python3

from cgi import FieldStorage
from random import shuffle
from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()
players = form_data.getfirst('players', '')

rsp_dict = {0: 'Dynamite', 1: 'Tornado', 2: 'Quicksand', 3: 'Pit', 4: 'Chain',
            5: 'Gun', 6: 'Law', 7: 'Whip', 8: 'Sword', 9: 'Rock',
            10: 'Death', 11: 'Wall', 12: 'Sun', 13: 'Camera',
            14: 'Fire', 15: 'Chainsaw', 16: 'School', 17: 'Scissors',
            18: 'Poison', 19: 'Cage', 20: 'Axe', 21: 'Peace', 22: 'Computer',
            23: 'Castle', 24: 'Snake', 25: 'Blood', 26: 'Porcupine',
            27: 'Vulture', 28: 'Monkey', 29: 'King', 30: 'Queen', 31: 'Prince',
            32: 'Princess', 33: 'Police', 34: 'Woman', 35: 'Baby', 36: 'Man',
            37: 'Home', 38: 'Train', 39: 'Car', 40: 'Noise', 41: 'Bicycle',
            42: 'Tree', 43: 'Turnip', 44: 'Duck', 45: 'Wolf', 46: 'Cat',
            47: 'Bird', 48: 'Fish', 49: 'Spider', 50: 'Cockroach', 51: 'Brain',
            52: 'Community', 53: 'Cross', 54: 'Money', 55: 'Vampire',
            56: 'Sponge', 57: 'Church', 58: 'Butter', 59: 'Book', 60: 'Paper',
            61: 'Cloud', 62: 'Aeroplane', 63: 'Moon', 64: 'Grass', 65: 'Film',
            66: 'Toilet', 67: 'Air', 68: 'Planet', 69: 'Guitar', 70: 'Bowl',
            71: 'Cup', 72: 'Beer', 73: 'Rain', 74: 'Water', 75: 'T.V.',
            76: 'Rainbow', 77: 'U.F.O.', 78: 'Alien', 79: 'Prayer',
            80: 'Mountain', 81: 'Satan', 82: 'Dragon', 83: 'Diamond',
            84: 'Platinum', 85: 'Gold', 86: 'Devil', 87: 'Fence',
            88: 'Video Game', 89: 'Maths', 90: 'Robot', 91: 'Heart',
            92: 'Electricity', 93: 'Lightning', 94: 'Medusa', 95: 'Power',
            96: 'Laser', 97: 'Nuke', 98: 'Sky', 99: 'Tank', 100: 'Helicopter'}

header = ''
form = '''<p class="again">
             <a href="https://cs1.ucc.ie/~cf26/game.html">Click here to play again</a>
          </p>'''

if len(form_data) != 0:
    try:
        header = 'Choose your weapon!'
        player1 = [key for key in rsp_dict]
        player2 = [key for key in rsp_dict]
        shuffle(player1)
        shuffle(player2)
        form = """
                <form action='rsp_game.py' type='get'>
                <fieldset>
                    <legend>Player 1</legend>"""
        for weapon in player1:
            form += """<input type="radio" name="rsp1" value="%s" id="%s" required />
            <label for="%s">%s</label>
            """ % (str(weapon), rsp_dict[weapon]+'1', rsp_dict[weapon]+'1', rsp_dict[weapon])
        form += '</fieldset>'
        if players == '1':
            form += """
                <fieldset>
                    <legend>Player 2</legend>"""
            for weapon in player2:
                form += """<input type="radio" name="rsp2" value="%s" id="%s" required />
                <label for="%s">%s</label>
                """ % (str(weapon), rsp_dict[weapon]+'2', rsp_dict[weapon]+'2', rsp_dict[weapon])
            form += '</fieldset>'
        form += '<input type="submit"  /></form>'
    except ValueError:
        header = 'Oops! Please enter a number'
else:
    header = 'Oops!'

print('''
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <link rel="stylesheet" href="rsp.css" />
            <title>RSP | Players</title>
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
            </main>
        </body>
    </html>''' % (header, form))
