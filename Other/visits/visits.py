#!/usr/local/bin/python3

from cgitb import enable
enable()

from os import environ
from http.cookies import SimpleCookie

cookie = SimpleCookie()
http_cookie_header = environ.get('HTTP_COOKIE')
if not http_cookie_header:
    cookie['num_visits'] = 1
else:
    cookie.load(http_cookie_header)
    if 'num_visits' not in cookie:
        cookie['num_visits'] = 1
    else:
        cookie['num_visits'] = int(cookie['num_visits'].value) + 1
cookie['num_visits']['expires'] = 157680000
print(cookie)
print('Content-Type: text/html')
print()
print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Welcome!</title>
        </head>
        <body>
            <p>
                You have visited this page %s times.
            </p>
        </body>
    </html>""" % (cookie['num_visits'].value))
