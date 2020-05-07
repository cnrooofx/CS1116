#! /usr/local/bin/python3

from cgitb import enable
enable()

from cgi import FieldStorage
from html import escape
from time import strptime
import pymysql as db

print('Content-Type: text/html')
print()

form_data = FieldStorage()
outcome = ''

try:
    lect_date = escape(form_data.getfirst('lect_date', '').strip())
    student_id = escape(form_data.getfirst('student_ids', '').strip())
    if not lect_date or not student_id:
        outcome = '<p>Please fill out all fields in the form</p>'
    else:
        valid_date = ''
        try:
            valid_date = strptime(lect_date, '%Y-%m-%d')
        except ValueError:
            outcome += '<p>Sorry! Date format is not valid. Please use YYYY-MM-DD</p>'
        if type(student_id) != int:
            outcome += '<p>Sorry! Student id must be a number</p>'
        if outcome == '':
            connection = db.connect('my_server', 'me', 'my_password', 'my_db')
            cursor = connection.cursor(db.cursors.DictCursor)
            cursor.execute("""SELECT *
                              FROM attendance
                              WHERE student_id = %d""", (student_id))
            if cursor.rowcount == 0:
                outcome = '<p>Sorry! Student id number is not valid</p>'
            else:
                cursor.execute("""SELECT *
                                  FROM attendance
                                  WHERE student_id = %d
                                  AND lect_date = %s""", (student_id, valid_date))
                if cursor.rowcount != 0:
                    outcome = 'Sorry! Your attendance has already been recorded'
                else:
                    cursor.execute("""INSERT INTO attendance (lect_date, student_id)
                                      VALUES (%s, %d)""", (valid_date, student_id))
                    connection.commit()
                    outcome = '<p>Thank you! Your attendance has been recorded.</p>'
            cursor.close()
            connection.close()
except db.Error:
    outcome = 'Sorry! There seems to be a problem at the moment. Please try again later.'

print("""<!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" /> <title>Lecture Attendance</title>
        </head>
        <body>
            %s
        </body>
    </html>""" % (outcome))
