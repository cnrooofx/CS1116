#!/usr/local/bin/python3

from cgi import FieldStorage
import cgitb, html, pymysql, os, hashlib, time, shelve, http.cookies

print('Content-Type: text/html')
print()

input = FieldStorage()
message = input.getfirst('message')

morse = ""
morse_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
              'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
              'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
              'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--',
              'X':'-..-', 'Y':'-.--', 'Z':'--..', ' ': ' '}

for char in message:
    char = char.upper()
    if char in morse_dict:
        morse += morse_dict[char]

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Your message in Morse code</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>Original: </th><td>%s</td>
                </tr>
                <tr>
                    <th>Morse: </th><td>%s</td>
                </tr>
            </table>
        </body>
    </html>""" % (message, morse))
