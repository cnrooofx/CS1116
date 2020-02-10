#!/usr/local/bin/python3

from cgi import FieldStorage
from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()
players = form_data.getfirst('players', '')

outcome = ''

if len(form_data) != 0:
    try:
        form = '''
                <form action='rsp_game.py' type='get'>
                <fieldset>
                    <legend>Player 1</legend>
                    <input type="radio" name="rsp1" value="0" id="rock" checked />
                    <label for="rock">Rock</label>
                    <input type="radio" name="rsp1" value="1" id="fire" />
                    <label for="fire">Fire</label>
                    <input type="radio" name="rsp1" value="2" id="scissors" />
                    <label for="scissors">Scissors</label>
                    <input type="radio" name="rsp1" value="3" id="snake" />
                    <label for="snake">Snake</label>
                    <input type="radio" name="rsp1" value="4" id="human" />
                    <label for="human">Human</label>
                    <input type="radio" name="rsp1" value="5" id="tree" />
                    <label for="tree">Tree</label>
                    <input type="radio" name="rsp1" value="6" id="wolf" />
                    <label for="wolf">Wolf</label>
                    <input type="radio" name="rsp1" value="7" id="sponge" />
                    <label for="sponge">Sponge</label>
                    <input type="radio" name="rsp1" value="8" id="paper" />
                    <label for="paper">Paper</label>
                    <input type="radio" name="rsp1" value="9" id="air" />
                    <label for="air">Air</label>
                    <input type="radio" name="rsp1" value="10" id="water" />
                    <label for="water">Water</label>
                    <input type="radio" name="rsp1" value="11" id="dragon" />
                    <label for="dragon">Dragon</label>
                    <input type="radio" name="rsp1" value="12" id="devil" />
                    <label for="devil">Devil</label>
                    <input type="radio" name="rsp1" value="13" id="lightning" />
                    <label for="lightning">Lightning</label>
                    <input type="radio" name="rsp1" value="14" id="gun" />
                    <label for="gun">Gun</label>
                </fieldset>'''
        if players == '1':
            form += '''
                <fieldset>
                    <legend>Player 2</legend>
                    <input type="radio" name="rsp2" value="0" id="rock" checked />
                    <label for="rock">Rock</label>
                    <input type="radio" name="rsp2" value="1" id="fire" />
                    <label for="fire">Fire</label>
                    <input type="radio" name="rsp2" value="2" id="scissors" />
                    <label for="scissors">Scissors</label>
                    <input type="radio" name="rsp2" value="3" id="snake" />
                    <label for="snake">Snake</label>
                    <input type="radio" name="rsp2" value="4" id="human" />
                    <label for="human">Human</label>
                    <input type="radio" name="rsp2" value="5" id="tree" />
                    <label for="tree">Tree</label>
                    <input type="radio" name="rsp2" value="6" id="wolf" />
                    <label for="wolf">Wolf</label>
                    <input type="radio" name="rsp2" value="7" id="sponge" />
                    <label for="sponge">Sponge</label>
                    <input type="radio" name="rsp2" value="8" id="paper" />
                    <label for="paper">Paper</label>
                    <input type="radio" name="rsp2" value="9" id="air" />
                    <label for="air">Air</label>
                    <input type="radio" name="rsp2" value="10" id="water" />
                    <label for="water">Water</label>
                    <input type="radio" name="rsp2" value="11" id="dragon" />
                    <label for="dragon">Dragon</label>
                    <input type="radio" name="rsp2" value="12" id="devil" />
                    <label for="devil">Devil</label>
                    <input type="radio" name="rsp2" value="13" id="lightning" />
                    <label for="lightning">Lightning</label>
                    <input type="radio" name="rsp2" value="14" id="gun" />
                    <label for="gun">Gun</label>
                </fieldset>'''
        form += '''<input type="submit"  /></form>'''
    except ValueError:
        outcome = 'Error! Please enter a number'
else:
    outcome = 'Error!'
    form = '''<p>
                 <a href="https://cs1.ucc.ie/~cf26/game.html">Click here to play again</a>
              </p>'''

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
    </html>''' % (outcome, form))
