#!/usr/local/bin/python3

from os import environ
from shelve import DbfilenameShelf
from http.cookies import SimpleCookie

from cgitb import enable
enable()

print('Content-Type: text/html')
print()

result = """<section>
       <strong>You are not logged in.</strong>
       <p>Please log in or create an account to play.</p>
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
                    <p>
                        Hey, %s. We hope you enjoy this photo!
                    </p>
                    <img src="photo1.jpg">
                    <ul>
                        <li><a href="protected_page_A.py">Web Dev 2 - Members Only A</a></li>
                        <li><a href="logout.py">Logout</a></li>
                    </ul>""" % session_store.get('username')
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
            <title>Play &vert; Game</title>
        </head>
        <body>
            <header>
                <h1>Game</h1>
                <nav>
                    <ul>
                        <li>
                            <a href="index.html">Home</a>
                        </li>
                        <li>
                            <a href="">Play</a>
                        </li>
                        <li>
                            <a href="leaderboard.py">Leaderboard</a>
                        </li>
                        <li>
                            <a href="account.py">Account</a>
                        </li>
                    </ul>
                </nav>
            </header>
            <main>
                %s
            </main>
        </body>
    </html>""" % (result))
