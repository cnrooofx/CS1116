#!/usr/local/bin/python3

from cgi import FieldStorage

print('Content-Type: text/html')
print()

form_data = FieldStorage()
fname = form_data.getfirst('firstname')
sname = form_data.getfirst('surname')

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Response</title>
        </head>
        <body>
            <p>
                Hello, %s %s. You may go on your way.
            </p>
        </body>
    </html>""" % (fname, sname))
