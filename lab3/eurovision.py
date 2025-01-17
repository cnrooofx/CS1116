#!/usr/local/bin/python3

from cgi import FieldStorage
import pymysql as db
from math import ceil
from html import escape
from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()
country = escape(form_data.getfirst('country', '')).strip()
points = escape(form_data.getfirst('points', '')).strip()

form = ''
output = ''

try:
    connection = db.connect('localhost', 'cf26', 'pecah', 'cs6503_cs1106_cf26')
    # connection = db.connect('localhost', 'cf26', 'p', 'cs6503_cs1106_cf26')
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""SELECT DISTINCT country FROM winners""")
    form = """<form action="eurovision.py" method="get">
        <label for="country">Search by Country:</label>
        <select name="country" id="country">
            <option value="" label="Please select a country"></option>"""
    for row in cursor.fetchall():
        if row['country'] == country:
            form += """<option value="%s" selected>%s</option>""" % (row['country'], row['country'])
        else:
            form += """<option value="%s">%s</option>""" % (row['country'], row['country'])
    else:
        form += """</select>
        <label for="points">And/Or Minimum Points:</label>
        <input type="text" name="points" value="%s" id="points" maxlength="3" size="5" />
        <input type="submit" value="Search" />
    </form>""" % (points)
    cursor.close()
    connection.close()
except db.Error:
    form = """<form action="eurovision.py" method="get">
            <label for="country">Search by Country:</label>
            <input type="text" name="country" value="%s" id="country" placeholder="e.g. Ireland" maxlength="25" />
            <label for="points">And/Or Minimum Points:</label>
            <input type="text" name="points" value="%s" id="points" maxlength="3" size="5" />
        <input type="submit" />
    </form>""" % (country, points)

if len(form_data) != 0:
    try:
        connection = db.connect('localhost', 'cf26', 'pecah', 'cs6503_cs1106_cf26')
        # connection = db.connect('localhost', 'cf26', 'p', 'cs6503_cs1106_cf26')
        cursor = connection.cursor(db.cursors.DictCursor)
        if points:
            points = ceil(float(points))
        else:
            points = 0
        country_name = ''
        if not country:
            country_name = '<th scope="col">Country</th>'
            if points > 0:
                caption = 'Eurovision Winners with at least %s Points' % (points)
                cursor.execute("""SELECT * FROM winners WHERE points >= %s""", (points))
            else:
                caption = 'Eurovision Winners'
                cursor.execute("""SELECT * FROM winners""")
        elif not points:
            caption = 'Eurovision Winners from %s' % (country)
            cursor.execute("""SELECT * FROM winners
                            WHERE country = %s""", (country))
        else:
            if points > 0:
                caption = 'Eurovision Winners from %s with at least %s Points' % (country.capitalize(), points)
                cursor.execute("""SELECT * FROM winners
                                WHERE country = %s AND points >= %s""", (country, points))
            else:
                caption = 'Eurovision Winners from %s' % (country)
                cursor.execute("""SELECT * FROM winners WHERE country = %s""", (country.capitalize()))
        if cursor.rowcount != 0:
            output = """<section>
            <table>
                <caption>%s</caption>
                <tr>
                    <th scope="col">Year</th>
                    %s
                    <th scope="col">Song</th>
                    <th scope="col">Performer</th>
                    <th scope="col">Points</th>
                </tr>""" % (caption, country_name)
            if country_name != '':
                for row in cursor.fetchall():
                    output += """<tr>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                </tr>""" % (row['year'], row['country'], row['song'], row['performer'], row['points'])
                output += """</table>
            </section>"""
            else:
                for row in cursor.fetchall():
                    output += """<tr>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                </tr>""" % (row['year'], row['song'], row['performer'], row['points'])
                output += """</table>
            </section>"""
        else:
            output = '<p>Sorry! There are no results matching your search. Please try again</p>'
        cursor.close()
        connection.close()
    except db.Error:
        output = '<p>Sorry. We are experiencing problems at the moment, please try again later.</p>'
    except ValueError:
        output = '<p>Error! Please enter a number for Points</p>'

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="initial-scale=1.0, width=device-width" />
            <link rel="stylesheet" href="styles.css" />
            <title>Eurovision Search</title>
        </head>
        <body>
            <header>
                <h1>Eurovision Winners Search</h1>
            </header>
            <main>
                %s
                %s
            </main>
        </body>
    </html>""" % (form, output))
