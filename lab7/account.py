#!/usr/local/bin/python3

from os import environ
from shelve import DbfilenameShelf
from http.cookies import SimpleCookie

from cgitb import enable
enable()

print('Content-Type: text/html')
print()

result = """
    <section>
        <p>You are not logged in.</p>
        <ul>
            <li><a href="login.py">Login</a></li>
            <li><a href="accounts/register.py">Register</a></li>
        </ul>
    </section>"""

try:
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if http_cookie_header:
        cookie.load(http_cookie_header)
        if 'sid' in cookie:
            sid = cookie['sid'].value
            session_store = DbfilenameShelf('sessions/sess_' + sid, writeback=False)
            if session_store.get('authenticated'):
                result = """
                <section>
                    <h2>My Account</h2>
                    <p>
                        Hey, %s.
                    </p>
                    <ul>
                        <li><a href="changepswd.py">Change password</a></li>
                        <li><a href="logout.py">Logout</a></li>
                        <li><a href="delete_account.py">Delete Account</a></li>
                    </ul>
                </section>""" % session_store.get('username')
            session_store.close()
except IOError:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <link rel="stylesheet" href="styles.css" />
            <meta name="viewport" content="initial-scale=1.0, width=device-width" />
            <title>Account Management</title>
        </head>
        <body>
            <header>
                <h1>Title</h1>
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
                        <a href="">Account</a>
                    </li>
                </ul>
            </nav>
            <main>
                %s
            </main>
        </body>
    </html>""" % (result))
