#!/usr/local/bin/python3

from cgi import FieldStorage
from random import randint
from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()
players = form_data.getfirst('players', '')
choice1 = form_data.getfirst('rsp1', '')
choice2 = form_data.getfirst('rsp2', '')

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
form = ''

if len(form_data) != 0:
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
    if len(choice1) != 0 or len(choice2) != 0:
        try:
            name1 = 'Player 1\'s'
            player1 = int(choice1)
            if players == '0':
                player2 = randint(0, 14)
                name2 = 'Computer\'s'
            elif players == '1':
                player2 = int(choice2)
                name2 = 'Player 2\'s'
            if player1 in rsp_dict:
                player1_out = rsp_dict[player1]
                player2_out = rsp_dict[player2]
                if player1 != player2:
                    i = 0
                    while i <= 7:
                        if player2 == ((player1 + i) % 15):
                            if (player1 == 6 and player2 == 12) or (player1 == 7 and player2 == 9):
                                extras = extras_dict[player2][player2]
                            outcome = '%s %s %s %s %s%s' % (name1, player1_out, beats_dict[player1][player2], name2, player2_out, extras)
                            break
                        i += 1
                    else:
                        if (player2 == 6 and player1 == 12) or (player2 == 7 and player1 == 9):
                            extras = extras_dict[player2][player1]
                        outcome = '%s %s %s %s %s%s' % (name2, player2_out, beats_dict[player2][player1], name1,  player1_out, extras)
                else:
                    outcome = '%s %s ties with %s %s' % (name2, player2_out, name1, player1_out)
            else:
                outcome = 'Error! Incorrect number'
        except ValueError:
            outcome = 'Error! Please enter a number'
else:
    form = '''
            <form action="rsp_game.py" method="get">
                <input type="radio" name="players" value="0" id="computer">
                <label for="computer">Player vs Computer</label>
                <input type="radio" name="players" value="1" id="player">
                <label for="player">Player vs Player</label>
                <input type="submit" />
            </form>'''


print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <link rel="stylesheet" href="lengths.css" />
            <title>Lengths</title>
        </head>
        <body>
            %s
            <p>
                %s
            </p>
        </body>
    </html>""" % (form, outcome))
