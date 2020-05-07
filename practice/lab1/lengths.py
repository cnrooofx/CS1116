#! usr/local/bin/python3

from cgi import FieldStorage, escape

from cgitb import enable
enable()

print('Content-Type: text/html')
print()

form_data = FieldStorage()

inches = 0.0
feet = 0.0
yards = 0.0

units = escape(form_data.getfirst('units', '').strip())

if units in ['feet', 'yards', 'inches']:


print("""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Lengths</title>
    </head>
    <body>
        <table>
            <tr>
                <th scope="row">
                    Inches:
                </th>
                <td>
                    %s
                </td>
            </tr>
            <tr>
                <th scope="row">
                    Feet:
                </th>
                <td>
                    %s
                </td>
            </tr>
            <tr>
                <th scope="row">
                    Yards:
                </th>
                <td>
                    %s
                </td>
            </tr>
        </table>
    </body>
</html>""" % (inches, feet, yards))