#!/usr/local/bin/python3

from os import environ
from shelve import open
from hashlib import sha256
from time import time
from http.cookies import SimpleCookie
from cgi import FieldStorage, escape
import pymysql as db

from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()
username = ''
error = ''
result = """
    <p>You are not logged in.</p>
    <form action="account.py" method="post">
        <fieldset>
            <legend>Login</legend>
            <label for="username">User name: </label>
            <input type="text" name="username" id="username" value="%s" />
            <label for="password">Password: </label>
            <input type="password" name="password" id="password" />
            <input type="submit" value="Login" />
       </fieldset>
    </form>
    <p>
        %s
    </p>
   <ul>
        <li><a href="accounts/register.py">Register</a></li>
        <li><a href="accounts/forgot.py">Forgot password</a></li>
   </ul>""" % (username, error)

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
    if len(form_data) != 0:
        username = escape(form_data.getfirst('username', '').strip())
        password = escape(form_data.getfirst('password', '').strip())
        if not username or not password:
            error = '<p>Error: user name and password are required</p>'
        else:
            sha256_password = sha256(password.encode()).hexdigest()
            try:
                connection = db.connect('localhost', 'cf26', 'pecah', 'cs6503_cs1106_cf26')
                cursor = connection.cursor(db.cursors.DictCursor)
                cursor.execute("""SELECT * FROM users
                                  WHERE username = %s
                                  AND password = %s""", (username, sha256_password))
                if cursor.rowcount == 0:
                    error = '<p>Error: incorrect user name or password</p>'
                else:
                    cookie = SimpleCookie()
                    sid = sha256(repr(time()).encode()).hexdigest()
                    cookie['sid'] = sid
                    session_store = open('sess_' + sid, writeback=True)
                    session_store['authenticated'] = True
                    session_store['username'] = username
                    session_store.close()
                    result = """
                       <p>Succesfully logged in!</p>
                       <p>Welcome back to Web Dev 2.</p>
                       <ul>
                           <li><a href="protected_page_A.py">Web Dev 2 - Members Only A</a></li>
                           <li><a href="protected_page_B.py">Web Dev 2 - Members Only B</a></li>
                           <li><a href="logout.py">Logout</a></li>
                       </ul>"""
                    print(cookie)
                cursor.close()
                connection.close()
            except (db.Error, IOError):
                error = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'
except IOError:
    error = '<p>Sorry! We are experiencing problems at the moment. Please try again later.</p>'

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
