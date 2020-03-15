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
        <li><a href="accounts/login.py">Login</a></li>
        <li><a href="accounts/register.py">Register</a></li>
   </ul>"""

if len(form_data) != 0:
    try:
        old_password = escape(form_data.getfirst('old_password', '').strip())
        password1 = escape(form_data.getfirst('password1', '').strip())
        password2 = escape(form_data.getfirst('password2', '').strip())
        if not old_password or not password1 or not password2:
            result = '<p>Error: user name and password are required</p>'
        cookie = SimpleCookie()
        http_cookie_header = environ.get('HTTP_COOKIE')
        if http_cookie_header:
            cookie.load(http_cookie_header)
            if 'sid' in cookie:
                sid = cookie['sid'].value
                session_store = open('sess_' + sid, writeback=False)
                if session_store.get('authenticated'):
                    result = """
                        <p>
                            Hey, %s. We hope you enjoy this photo!
                        </p>
                        <img src="photo1.jpg">
                        <ul>
                            <li><a href="protected_page_A.py">Web Dev 2 - Members Only A</a></li>
                            <li><a href="changepswd.py">Change password</a></li>
                            <li><a href="logout.py">Logout</a></li>
                        </ul>""" % session_store.get('username')
                session_store.close()
    except IOError:
        result = '<p>Sorry! We are experiencing problems at the moment. Please try again later.</p>'

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Web Dev 2</title>
        </head>
        <body>
            %s
        </body>
    </html>""" % (result))
