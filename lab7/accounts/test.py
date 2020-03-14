from passwordgen import generate_password
from send_email import password_email

name = 'Conor FOx'
password = generate_password()

password_email(name, password)
