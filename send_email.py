from email.mime.text import MIMEText
import smtplib

def send_email(email, height_,average_height,count):
    from_email="YOUR EMAIL-ID"
    from_password="YOUR PASSWORD"
    to_email=email

    subject="Height data"
    message="Hey there, your height is <strong>%s</strong>.<br> Average height is <strong>%s</strong> and that is calculated out of <strong>%s</strong> peoples. <br> Thank you!!" % (height_,average_height,count)

    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']= from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
