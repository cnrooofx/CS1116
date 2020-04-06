
import smtplib
import ssl


def password_email(username, email, password):
    context = ssl.create_default_context()
    sender_email = "conorfox.test@gmail.com"
    message = """From: %s
    To: %s
    Subject: Complete your registration

    Hey %s,

    Thank you for registering.

    Your password is:

    %s

    You can change it later in the account page.

    Thanks,
        Conor
    """ % (sender_email, email, username, password)

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
        server.login(sender_email, '+4xmsXrn;Jn2aCQk')
        server.sendmail(sender_email, email, message)

    # with smtplib.SMTP("localhost", 1025) as server:
    #     server.sendmail(sender_email, receiver_email, message)


def reset_email(username, email, code):
    context = ssl.create_default_context()
    sender_email = "conorfox.test@gmail.com"
    message = """From: %s
    To: %s
    Subject: Password Reset

    Hey %s,

    A password reset has been requested.

    Your code is:
    
    %s

    If you didn't request this, you can safely ignore this email.

    Thanks,
        Conor
    """ % (sender_email, email, username, code)

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
        server.login(sender_email, '+4xmsXrn;Jn2aCQk')
        server.sendmail(sender_email, email, message)
