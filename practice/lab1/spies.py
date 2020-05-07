#! /usr/local/bin/python3

from cgi import FieldStorage, escape

from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()

fname = escape(form_data.getfirst('fname', '').strip())
sname = escape(form_data.getfirst('sname', '').strip())

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Spies</title>
        </head>
        <body>
            <p>
                Your spy name is: %s, %s %s.
            </p>
        </body>
    </html>""" % (sname, fname, sname))
