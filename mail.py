import smtplib, ssl
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "test12mail98@gmail.com"  # Enter your address
receiver_email = "vidyapunjabi7@gmail.com"  # Enter receiver address
password = "testmail!@98"
messagemail = ("Subject: Admission query \n\n"+"hello")

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, messagemail)
