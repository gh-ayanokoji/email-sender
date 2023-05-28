from email.message import EmailMessage
import ssl
import smtplib

#enter your email address here
sender = ''

#create an app password in your email and enter it here
#DO NOT ENTER YOUR ORIGINAL PASSWORD
password = ''

#rest of the code you can use it as is
receiver = input("enter the email id of the receiver : ")

subject = input('enter your subject : ')

body = input('enter your message body:')

em = EmailMessage()
em['from'] = sender
em['to'] = receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, em.as_string())
