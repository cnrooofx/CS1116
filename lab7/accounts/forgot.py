#!/usr/local/bin/python3

from cgi import FieldStorage, escape
from os import environ
from shelve import DbfilenameShelf
from time import time
from hashlib import sha256
from random import randint
import pymysql as db
from http.cookies import SimpleCookie

from passwordgen import generate_password
from send_email import reset_email

from cgitb import enable
enable()

form_data = FieldStorage()

form = """<form action="forgot.py" method="post">
    <label for="username">Username: </label>
    <input type="text" name="username" id="username" value="" />
    <input type="submit" value="Reset Password" />
</form>"""
result = ''

if len(form_data) != 0:
    try:
        cookie = SimpleCookie()
        http_cookie_header = environ.get('HTTP_COOKIE')
        if http_cookie_header:
            cookie.load(http_cookie_header)
            if 'reset' in cookie:
                sid = cookie['reset'].value
                code = escape(form_data.getfirst('code', '').strip())
                session_store = DbfilenameShelf('../sessions/reset_' + sid, writeback=False)
                if session_store.get('code') == code:
                    new_password = generate_password()
                    sha256_password = sha256(new_password.encode()).hexdigest()
                    result = str(sha256_password)
                else:
                    form = """<form action="forgot.py" method="post">
                            <label for="code">Code: </label>
                            <input type="number" name="code" id="code" min="0" max="99999" />
                            <imput type="submit" />
                        </form>
                    <p><strong>Error! Incorrect code.</strong></p>"""
        # if code and not username:
        #
        #     new_password = generate_password()
        #     sha256_password = sha256(new_password.encode()).hexdigest()
            else:
                username = escape(form_data.getfirst('username', '').strip())
                if not username:
                    result = '<p><strong>Error! Please enter a username.</strong></p>'
                else:
                    connection = db.connect('localhost', 'cf26', 'pecah', 'cs6503_cs1106_cf26')
                    cursor = connection.cursor(db.cursors.DictCursor)
                    cursor.execute("""SELECT email
                                      FROM users
                                      WHERE username = %s""", username)
                    if cursor.rowcount != 0:
                        email = cursor.fetchone()['email']
                        sid = sha256(repr(time()).encode()).hexdigest()
                        code = ''
                        for i in range(5):
                            code += str(randint(0, 9))
                        session_store = DbfilenameShelf('../sessions/reset_' + sid, writeback=True)
                        session_store['username'] = username
                        session_store['code'] = code
                        cookie['reset'] = sid
                        print(cookie)
                        reset_email(username, email, code)
                        session_store.close()
                    form = """<form action="forgot.py" method="post">
                        <label for="code">Code: </label>
                        <input type="number" name="code" id="code" />
                        <imput type="submit" />
                    </form>"""
                    result = '<p>Please check your email for the password reset code.</p>'
                    cursor.close()
                    connection.close()
    except (db.Error, IOError):
        result = '<p>Sorry! We are experiencing problems at the moment. Please try again later.</p>'

print('Content-Type: text/html')
print()

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <link rel="stylesheet" href="../styles.css" />
            <meta name="viewport" content="initial-scale=1.0, width=device-width" />
            <title>Login</title>
        </head>
        <body>
            <header>
                <h1>Game</h1>
                <nav>
                    <ul>
                        <li>
                            <a href="../index.html">Home</a>
                        </li>
                        <li>
                            <a href="../game.py">Game</a>
                        </li>
                        <li>
                            <a href="../leaderboard.py">Leaderboard</a>
                        </li>
                        <li>
                            <a href="../account.py">Account</a>
                        </li>
                    </ul>
                </nav>
            </header>
            <main>
                <section>
                    <h2>Reset Password</h2>
                    %s
                    %s
                </section>
            </main>
        </body>
    </html>""" % (form, result))
