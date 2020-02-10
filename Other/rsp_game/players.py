#!/usr/local/bin/python3

from cgi import FieldStorage
from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()
players = form_data.getfirst('players', '')

header = ''
form = '''<p>
             <a href="https://cs1.ucc.ie/~cf26/game.html">Click here to play again</a>
          </p>'''

if len(form_data) != 0:
    try:
        header = 'Choose your weapon!'
        form = '''
                <form action='rsp_game.py' type='get'>
                <fieldset>
                    <legend>Player 1</legend>
                    <input type="radio" name="rsp1" value="0" id="rock1" checked />
                    <label for="rock1">Rock</label>
                    <input type="radio" name="rsp1" value="1" id="fire1" />
                    <label for="fire1">Fire</label>
                    <input type="radio" name="rsp1" value="2" id="scissors1" />
                    <label for="scissors1">Scissors</label>
                    <input type="radio" name="rsp1" value="3" id="snake1" />
                    <label for="snake1">Snake</label>
                    <input type="radio" name="rsp1" value="4" id="human1" />
                    <label for="human1">Human</label>
                    <input type="radio" name="rsp1" value="5" id="tree1" />
                    <label for="tree1">Tree</label>
                    <input type="radio" name="rsp1" value="6" id="wolf1" />
                    <label for="wolf1">Wolf</label>
                    <input type="radio" name="rsp1" value="7" id="sponge1" />
                    <label for="sponge1">Sponge</label>
                    <input type="radio" name="rsp1" value="8" id="paper1" />
                    <label for="paper1">Paper</label>
                    <input type="radio" name="rsp1" value="9" id="air1" />
                    <label for="air1">Air</label>
                    <input type="radio" name="rsp1" value="10" id="water1" />
                    <label for="water1">Water</label>
                    <input type="radio" name="rsp1" value="11" id="dragon1" />
                    <label for="dragon1">Dragon</label>
                    <input type="radio" name="rsp1" value="12" id="devil1" />
                    <label for="devil1">Devil</label>
                    <input type="radio" name="rsp1" value="13" id="lightning1" />
                    <label for="lightning1">Lightning</label>
                    <input type="radio" name="rsp1" value="14" id="gun1" />
                    <label for="gun1">Gun</label>
                </fieldset>'''
        if players == '1':
            form += '''
                <fieldset>
                    <legend>Player 2</legend>
                    <input type="radio" name="rsp2" value="0" id="rock2" checked />
                    <label for="rock2">Rock</label>
                    <input type="radio" name="rsp2" value="1" id="fire2" />
                    <label for="fire2">Fire</label>
                    <input type="radio" name="rsp2" value="2" id="scissors2" />
                    <label for="scissors2">Scissors</label>
                    <input type="radio" name="rsp2" value="3" id="snake2" />
                    <label for="snake2">Snake</label>
                    <input type="radio" name="rsp2" value="4" id="human2" />
                    <label for="human2">Human</label>
                    <input type="radio" name="rsp2" value="5" id="tree2" />
                    <label for="tree2">Tree</label>
                    <input type="radio" name="rsp2" value="6" id="wolf2" />
                    <label for="wolf2">Wolf</label>
                    <input type="radio" name="rsp2" value="7" id="sponge2" />
                    <label for="sponge2">Sponge</label>
                    <input type="radio" name="rsp2" value="8" id="paper2" />
                    <label for="paper2">Paper</label>
                    <input type="radio" name="rsp2" value="9" id="air2" />
                    <label for="air2">Air</label>
                    <input type="radio" name="rsp2" value="10" id="water2" />
                    <label for="water2">Water</label>
                    <input type="radio" name="rsp2" value="11" id="dragon2" />
                    <label for="dragon2">Dragon</label>
                    <input type="radio" name="rsp2" value="12" id="devil2" />
                    <label for="devil2">Devil</label>
                    <input type="radio" name="rsp2" value="13" id="lightning2" />
                    <label for="lightning2">Lightning</label>
                    <input type="radio" name="rsp2" value="14" id="gun2" />
                    <label for="gun2">Gun</label>
                </fieldset>'''
        form += '''<input type="submit"  /></form>'''
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
            <h1>
                %s
            </h1>
            %s
        </body>
    </html>''' % (header, form))
