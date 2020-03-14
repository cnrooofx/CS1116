#!/usr/local/bin/python3

from cgi import FieldStorage, escape
from hashlib import sha256
import pymysql as db
from passwordgen import generate_password
from send_email import password_email

from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()
name = ''
username = ''
email = ''
result = ''

if len(form_data) != 0:
    name = escape(form_data.getfirst('name', '').strip())
    username = escape(form_data.getfirst('username', '').strip())
    email = escape(form_data.getfirst('email', '').strip())
    if not name or not username or not email:
        result = '<p>Sorry! All fields are required.</p>'
    else:
        try:
            connection = db.connect('localhost', 'cf26', 'pecah', 'cs6503_cs1106_cf26')
            cursor = connection.cursor(db.cursors.DictCursor)
            cursor.execute("""SELECT * FROM users
                              WHERE username = %s""", (username))
            if cursor.rowcount > 0:
                result = """<p>Sorry! That username is already taken.</p>
                            <p>Choose another username or <a href='login.py'>Click here</a> to sign in.</p>"""
            else:
                password = generate_password()
                sha256_password = sha256(password.encode()).hexdigest()
                cursor.execute("""INSERT INTO users (username, name, email, password)
                                  VALUES (%s, %s, %s, %s)""", (username, name, email, sha256_password))
                connection.commit()
                cursor.close()
                connection.close()
                password_email(name, email, password)
                result = """
                   <p>You have been successfully registered!</p>
                   <p>Please check your email to get your password</p>"""
        except (db.Error, IOError):
            result = '<p>Sorry! We are experiencing problems at the moment. Please try again later.</p>'

print("""
    <!DOCTYPE html>
    <html lang='en'>
        <head>
            <meta charset='utf-8' />
            <title>Web Dev 2</title>
        </head>
        <body>
            <form action='register.py' method='post'>
                <fieldset>
                    <label for='name'>Name: </label>
                    <input type='text' name='name' id='name' value='%s' required />
                    <label for='username'>Username: </label>
                    <input type='text' name='username' id='username' value='%s' required />
                    <label for='email'>Email: </label>
                    <input type='email' name='email' id='email' value='%s' required />
                    <input type='submit' value='Register' />
                </fieldset>
            </form>
            %s
        </body>
    </html>""" % (name, username, email, result))
