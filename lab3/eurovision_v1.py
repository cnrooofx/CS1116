#!/usr/local/bin/python3

from cgi import FieldStorage
import pymysql as db
from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()

country = ''
output = ''

if len(form_data) != 0:
    try:
        country = form_data.getfirst('country', '')
        connection = db.connect('localhost', 'cf26', 'pecah', 'cs6503_cs1106_cf26')
        cursor = connection.cursor(db.cursors.DictCursor)
        cursor.execute("""SELECT * FROM winners WHERE country = %s""", (country))
        if len(cursor.fetchall()) != 0:
            output = """<table>
                <tr><th colspan="4">Eurovision Winners</th></tr>
                <tr><th>Year</th><th>Song</th><th>Performer</th><th>Points</th></tr>"""
            for row in cursor.fetchall():
                print(len(row))
                output += """<tr>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                            </tr>""" % (row['year'], row['song'], row['performer'], row['points'])
            else:
                output += '</table>'
        else:
            output = 'Please enter a country in the Eurovision'
    except db.Error:
        output = 'Sorry. We are experiencing problems at the moment, please try again later.'

print("""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8" />
            <title>Eurovision</title>
        </head>
        <body>
            <form action="eurovision.py" method="get">
                <label for="country">Country: </label>
                <input type="text" name="country" value="%s" id="country" />
                <input type="submit" />
            </form>
            %s
        </body>
    </html>""" % (country, output))
