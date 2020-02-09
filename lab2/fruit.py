#!/usr/local/bin/python3

from cgi import FieldStorage
from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()
fruit_list = form_data.getlist('fruit')

fruit_dict = {'apples': 1.59, 'bananas': 1.25, 'jujubes': 27.81, 'rambutans': 20.84}
outcome = ''

try:
    total = 0
    for fruit in fruit_list:
        if fruit_list.count(fruit) == 1:
            total += fruit_dict[fruit]
    if total != 0:
        outcome = '%.2f' % (total)
    else:
        outcome = 'Error! Please select at least one fruit'
except KeyError:
    outcome = 'Error! That\'s not a valid option'

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
