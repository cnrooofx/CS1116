# from passwordgen import generate_password
# from send_email import password_email
from hashlib import sha256

# name = 'Conor FOx'
# password = generate_password()
#
# password_email(name, password)

password = 'conor.admin'

sha256_password = sha256(password.encode()).hexdigest()

print(sha256_password)
