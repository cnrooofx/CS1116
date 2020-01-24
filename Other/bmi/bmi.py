#!/usr/local/bin/python3

from cgitb import enable
enable()

from cgi import FieldStorage

print('Content-Type: text/html')
print()

form_data = FieldStorage()
mass_kg = form_data.getfirst('mass_kg', '').strip()
height_m = form_data.getfirst('height_m', '').strip()

outcome = ''
try:
    mass_kg = float(mass_kg)
    height_m = float(height_m)
    bmi = mass_kg / (height_m * height_m)
    category = ''
    if bmi < 18.5:
        category = 'underweight'
    elif bmi > 25:
        category ='overweight'
    else:
        category = 'normal'
    outcome = """Your mass in kg is %.1f. Your height in m is %.1f.
                 Your BMI is %.2f. You are %s.""" % (mass_kg, height_m, bmi, category)
except ValueError:
    outcome = 'You should enter numbers for your weight and height.'

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>BMI</title>
        </head>
        <body>
            <p>
                %s
            </p>
        </body>
    </html>""" % (outcome))
