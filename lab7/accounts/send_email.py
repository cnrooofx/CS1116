
import smtplib
import ssl


def password_email(username, email, password):
    context = ssl.create_default_context()
    sender_email = "conorfox.test@gmail.com"
    message = """Subject: Complete your registration

    Hey %s,

    Thank you for registering

    Your password is:
    %s

    You can change it later in the account page.

    Thanks,
        Conor
    """ % (username, password)

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
        server.login(sender_email, '+4xmsXrn;Jn2aCQk')
        server.sendmail(sender_email, email, message)

    # with smtplib.SMTP("localhost", 1025) as server:
    #     server.sendmail(sender_email, receiver_email, message)
