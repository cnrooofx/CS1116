#!/usr/local/bin/python3

from cgi import FieldStorage
import pymysql as db
from html import escape
from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()
country = escape(form_data.getfirst('country', '')).strip()
# country = form_data.getfirst('country', '')

form = ''
output = ''

try:
    connection = db.connect('localhost', 'cf26', 'pecah', 'cs6503_cs1106_cf26')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""SELECT DISTINCT country FROM winners""")
    for row in cursor.fetchall():
        if row['country'] == country:
            form += """<option value="%s" selected>%s</option>""" % (row['country'], row['country'])
        else:
            form += """<option value="%s">%s</option>""" % (row['country'], row['country'])
    if len(form_data) != 0:
        cursor.execute("""SELECT * FROM winners WHERE country = %s""", (country))
        if cursor.rowcount != 0:
            output = """<table>
                <tr><th colspan="4">Eurovision Winners from %s</th></tr>
                <tr><th>Year</th><th>Song</th><th>Performer</th><th>Points</th></tr>""" % (country)
            for row in cursor.fetchall():
                output += """<tr>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                            </tr>""" % (row['year'], row['song'], row['performer'], row['points'])
            else:
                output += '</table>'
        else:
            output = '<p>Please enter a country in the Eurovision</p>'
    cursor.close()
    connection.close()
except db.Error:
    output = '<p>Sorry. We are experiencing problems at the moment, please try again later.</p>'

print("""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8" />
            <title>Eurovision</title>
        </head>
        <body>
            <form action="eurovision.py" method="get">
                <label for="country">Select a Country</label>
                <select name="country" id="country">
                    %s
                </select>
                <input type="submit" />
            </form>
            %s
        </body>
    </html>""" % (form, output))
