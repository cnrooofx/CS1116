#!/usr/local/bin/python3

from cgi import FieldStorage
from html import escape
from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()
length = escape(form_data.getfirst('length', '')).strip()
units = escape(form_data.getfirst('units', '')).strip()

output = ''
inches = 0.0
yards = 0.0
feet = 0.0

if units in ['feet', 'inches', 'yards']:
    try:
        if units == 'feet':
            feet = float(length)
            inches = feet * 12
            yards = feet / 3
        elif units == 'inches':
            inches = float(length)
            feet = inches / 12
            yards = inches / 36
        else:
            yards = float(length)
            inches = yards * 36
            feet = yards * 3
        output = """ <table>
                    <tr>
                        <th colspan="2" scope="col">Results</th>
                    </tr>
                    <tr>
                        <th scope="row">Inches:</th>
                        <td>%.2f</td>
                    </tr>
                    <tr>
                        <th scope="row">Feet:</th>
                        <td>%.2f</td>
                    </tr>
                    <tr>
                        <th scope="row">Yards:</th>
                        <td>%.2f</td>
                    </tr>
                </table>""" % (inches, feet, yards)
    except ValueError:
        output = '<p>Error! Please enter a number</p>'
else:
    output = '<p>Error! Invalid units</p>'


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
        </body>
    </html>""" % (output))
