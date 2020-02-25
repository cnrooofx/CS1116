#!/usr/local/bin/python3

from cgi import FieldStorage
import pymysql as db
from html import escape
from os import environ
from http.cookies import SimpleCookie

from cgitb import enable
enable()

cookie = SimpleCookie()
http_cookie_header = environ.get('HTTP_COOKIE')

voted = ''
if not http_cookie_header:
    cookie['vote'] = 'yes'
else:
    cookie.load(http_cookie_header)
    if 'vote' not in cookie:
        cookie['vote'] = 'yes'
    else:
        voted = cookie['vote'].value
        cookie['vote'] = 'yes'
cookie['vote']['expires'] = 157680000
print(cookie)

print('Content-Type: text/html')
print()

form_data = FieldStorage()
output = ''

if voted == 'yes':
    output = 'You have already submitted your vote.'
else:
    try:
        name = escape(form_data.getfirst('candidate_name', '')).strip()
        connection = db.connect('localhost', 'cf26', 'pecah', 'cs6503_cs1106_cf26')
        cursor = connection.cursor(db.cursors.DictCursor)
        cursor.execute("""SELECT * FROM candidates
                          WHERE candidate_name = %s""", name)
        if cursor.rowcount != 0:
            cursor.execute("""UPDATE candidates
                              SET total_votes = total_votes + 1
                              WHERE candidate_name = %s""", name)
            connection.commit()
            output = 'Thank you. Your vote for %s has been successfully submitted.' % (name)
        else:
            output = 'Error! Candidate does not exist.'
        cursor.close()
        connection.close()
    except db.Error:
        output = 'Sorry. We are experiencing problems at the moment, please try again later.'

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Voting</title>
        </head>
        <body>
            <p>
                %s
            </p>
        </body>
    </html>""" % (output))
