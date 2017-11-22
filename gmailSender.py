import smtplib

import sys
from getpass import getpass

from pip._vendor.distlib.compat import raw_input


def send_email(user, pwd, recipient, subject, body):
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except Exception as e:
        print(e)
        print("failed to send mail")


if __name__ == '__main__':
    # SMTP_SSL Example
    try:
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo()  # optional, called by login()

        gmail_user = raw_input("Please enter email address: ")
        gmail_pwd = getpass('Password:')
        send_email(gmail_user, gmail_pwd, "mahmed27@uncc.edu", "test", "Hello Mod!")

        # server_ssl.login(gmail_user, gmail_pwd)
        # ssl server doesn't support or need tls, so don't call server_ssl.starttls()
        # server_ssl.sendmail(FROM, TO, message)
        # server_ssl.quit()
        # server_ssl.close()
        # print('successfully sent the mail')
    except Exception as e:
        print(e)
