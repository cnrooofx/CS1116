#!/usr/local/bin/python3

from cgitb import enable
enable()

from cgi import FieldStorage
from math import pi

print('Content-Type: text/html')
print()

form_data = FieldStorage()

outcome = ""
circumference_input = ""
hat_size = 0.0
if len(form_data) != 0:
    circumference_input = escape(form_data.getfirst("circumference"))
    try:
        circumference = float(circumference_input)
        hat_size = circumference / pi
    except ValueError:
        outcome = "<p>Error!</p>"



print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Big head</title>
        </head>
        <body>
            <form action="head_to_hat.py" method="get">
                <label for="circumference">Circumference: </label>
                <input type="text" name="circumference" id="circumference" value="%s" />
                <label for="hat_size">Hat size: </label>
                <input type="text" name="hat_size" id="hat_size" value = "%f" disabled />
                <input type="submit" />
            </form>
            %s
        </body>
    </html>""" % (circumference_input, hat_size, outcome))
