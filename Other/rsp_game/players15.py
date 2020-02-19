#!/usr/local/bin/python3

from cgi import FieldStorage
from random import shuffle
from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()
players = form_data.getfirst('players', '')

rsp_dict = {0: 'Rock', 1: 'Fire', 2: 'Scissors', 3: 'Snake', 4: 'Human',
            5: 'Tree', 6: 'Wolf', 7: 'Sponge', 8: 'Paper', 9: 'Air',
            10: 'Water', 11: 'Dragon', 12: 'Devil', 13: 'Lightning',
            14: 'Gun'}

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
                <form action='rsp15.py' type='get'>
                <label for="name1">Player 1 Name: </label>
                <input type="text" name="name1" value="" maxlength="15" size="15" id="name1" />
                <fieldset>
                    <legend>Player 1</legend>"""

        for weapon in player1:
            form += """<input type="radio" name="rsp1" value="%s" id="%s" required />
            <label for="%s">%s</label>
            """ % (str(weapon), rsp_dict[weapon]+'1', rsp_dict[weapon]+'1', rsp_dict[weapon])
        form += '</fieldset>'
        if players == '1':
            form += """<label for="name1">Player 2 Name: </label>
                <input type="text" name="name2" value="" maxlength="15" size="15" id="name2" />"""
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
