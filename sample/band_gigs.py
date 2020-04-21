#! usr/local/bin/python3


from cgitb import enable
enable()

from cgi import FieldStorage
from html import escape
from time import strptime
import pymysql as db

print('Content-Type: text/html')
print()

form_data = FieldStorage()

bandname = ''
gig_date = ''
result = ''

if len(form_data) != 0:
    bandname = escape(form_data.getfirst('bandname', '').strip())
    gig_date = escape(form_data.getfirst('gig_date', '').strip())
    try:
        valid_date = strptime(gig_date, '%Y-%m-%d')
        connection = db.connect('my_server', 'me', 'my_password', 'my_db')
        cursor = connection.cursor(db.cursors.DictCursor)
        if gig_date and not bandname:
            cursor.execute("""SELECT *
                              FROM gigs
                              WHERE gig_date >= %s""", valid_date)
            result = """<table>
                        <tr>
                            <th scope="col">Band Name</th>
                            <th scope="col">Gig Date</th>
                        </tr>"""
            for row in cursor.fetchall():
                result += """<tr>
                                <td>%s</td>
                                <td>%s</td>
                            </tr>""" % (row['bandname'], row['gig_date'])
            result += '</table>'
        else:
            cursor.execute("""SELECT *
                              FROM gigs
                              WHERE bandname = %s""", bandname)
            if cursor.rowcount != 0:
                if gig_date:
                    cursor.execute("""SELECT *
                                      FROM gigs
                                      WHERE bandname = %s
                                      AND gig_date >= %s""", bandname, valid_date)
                result = """<table>
                            <tr>
                                <th scope="col">Band Name</th>
                                <th scope="col">Gig Date</th>
                            </tr>"""
                for row in cursor.fetchall():
                    result += """<tr>
                                    <td>%s</td>
                                    <td>%s</td>
                                </tr>""" % (row['bandname'], row['gig_date'])
                result += '</table>'
            else:
                result = 'Error! There are no results for the band \'%s\'.' % bandname
        cursor.close()
        connection.close()
    except db.Error:
        result = 'There seems to be a problem at the moment. Please check back again later.'
    except ValueError:
        result = 'Error! Please enter a valid date in the form \'YYYY-MM-DD\''



print("""<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>Our Gigs</title>
            </head>
            <body>
                <form action="band_gigs.py" method="get"> <label>Band name: </label>
                <input type="text" name="bandname" value="%s" /> <label>Gig date (YYYY-MM-DD): </label>
                <input type="text" name="gig_date" value="%s" /> <input type="submit" value="Search for gigs" />
                </form>
                %s
            </body>
        </html>""" % (bandname, gig_date, result))