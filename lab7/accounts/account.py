#!/usr/local/bin/python3

from os import environ
from shelve import open
from http.cookies import SimpleCookie

from cgitb import enable
enable()

print('Content-Type: text/html')
print()

result = """
    <p>You are not logged in.</p>
    <ul>
        <li><a href="login.py">Login</a></li>
        <li><a href="register.py">Register</a></li>
    </ul>"""

try:
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:
        cookie.load(http_cookie_header)
        if 'sid' in cookie:
            sid = cookie['sid'].value
            session_store = open('sess_' + sid, writeback=False)
            if session_store.get('authenticated'):
                result = """
                    <h1>Account Management</h1>
                    <p>
                        Hey, %s.
                    </p>
                    <ul>
                        <li><a href="changepswd.py">Change password</a></li>
                        <li><a href="logout.py">Logout</a></li>
                        <li><a href="delete_account.py">Delete Account</a></li>
                    </ul>""" % session_store.get('username')
            session_store.close()
except IOError:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Account Management</title>
        </head>
        <body>
            %s
        </body>
    </html>""" % (result))
