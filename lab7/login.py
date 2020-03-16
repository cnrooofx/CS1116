#!/usr/local/bin/python3

from cgi import FieldStorage, escape
from hashlib import sha256
from time import time
from shelve import DbfilenameShelf
from http.cookies import SimpleCookie
import pymysql as db

from cgitb import enable
enable()

form_data = FieldStorage()
username = ''
error = ''
result = '<p><a href="accounts/forgot.py">Forgot password</a></p>'

if len(form_data) != 0:
    username = escape(form_data.getfirst('username', '').strip())
    password = escape(form_data.getfirst('password', '').strip())
    if not username or not password:
        error = '<p>Error! Both username and password are required</p>'
    else:
        sha256_password = sha256(password.encode()).hexdigest()
        try:
            connection = db.connect('localhost', 'cf26', 'pecah', 'cs6503_cs1106_cf26')
            cursor = connection.cursor(db.cursors.DictCursor)
            cursor.execute("""SELECT * FROM users
                              WHERE username = %s
                              AND password = %s""", (username, sha256_password))
            if cursor.rowcount == 0:
                error = '<p>Error! Incorrect user name or password</p>'
            else:
                cookie = SimpleCookie()
                sid = sha256(repr(time()).encode()).hexdigest()
                cookie['sid'] = sid
                session_store = DbfilenameShelf('sessions/sess_' + sid, writeback=True)
                session_store['authenticated'] = True
                session_store['username'] = username
                session_store.close()
                result = """
                   <p>Succesfully logged in!</p>
                   <section>
                       <h3>Welcome back!</h3>
                       <ul>
                           <li><a href="protected_page_A.py">Web Dev 2 - Members Only A</a></li>
                           <li><a href="protected_page_B.py">Web Dev 2 - Members Only B</a></li>
                           <li><a href="logout.py">Logout</a></li>
                       </ul>
                   </section>"""
                print(cookie)
            cursor.close()
            connection.close()
        except (db.Error, IOError):
            error = '<p>Sorry! We are experiencing problems at the moment. Please try again later.</p>'

print('Content-Type: text/html')
print()
print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <link rel="stylesheet" href="styles.css" />
            <meta name="viewport" content="initial-scale=1.0, width=device-width" />
            <title>Login</title>
        </head>
        <body>
            <header>
                <h1>Game</h1>
            </header>
            <nav>
                <ul>
                    <li>
                        <a href="index.html">Home</a>
                    </li>
                    <li>
                        <a href="game.py">Game</a>
                    </li>
                    <li>
                        <a href="leaderboard.py">Leaderboard</a>
                    </li>
                    <li>
                        <a href="account.py">Account</a>
                    </li>
                </ul>
            </nav>
            <main>
                <h2>Login</h2>
                <form action="login.py" method="post">
                    <label for="username">User name: </label>
                    <input type="text" name="username" id="username" value="%s" />
                    <label for="password">Password: </label>
                    <input type="password" name="password" id="password" />
                    <input type="submit" value="Login" />
                </form>
                %s
                %s
            </main>
        </body>
    </html>""" % (username, error, result))
