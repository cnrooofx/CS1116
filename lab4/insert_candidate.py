#!/usr/local/bin/python3

from cgi import FieldStorage
import pymysql as db
from html import escape

from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()

name = ''
output = ''

if len(form_data) != 0:
    try:
        name = escape(form_data.getfirst('name', '').strip())
        connection = db.connect('localhost', 'cf26', 'pecah', 'cs6503_cs1106_cf26')
        cursor = connection.cursor(db.cursors.DictCursor)
        cursor.execute("""SELECT candidate_name FROM candidates""")
        candidate_list = [candidate['candidate_name'] for candidate in cursor.fetchall()]
        if name not in candidate_list:
            cursor.execute("""INSERT INTO candidates VALUES (%s, 0)""", name)
            connection.commit()
            output = 'Candidate \'%s\' sucessfully submitted.' % (name)
        else:
            output = 'Error! Candidate already exists'
        cursor.close()
        connection.close()
    except db.Error:
        output = 'Sorry. We are experiencing problems at the moment, please try again later.'

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Insert Candidate</title>
        </head>
        <body>
            <form action="insert_candidate.py" method="post">
                <label for="name">Enter new candidates name: </label>
                <input type="text" name="name" value="%s" id="name">
                <input type="submit" />
            </form>
            <p>
                %s
            </p>
        </body>
    </html>""" % (name, output))
