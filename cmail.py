import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('kgeethikadevi2002@gmail.com','lwqz oqkv omub rnsi')
    msg=EmailMessage()
    msg['FROM']='kgeethikadevi2002@gmail.com'
    msg['SUBJECT']=subject
    msg['TO']=to
    msg.set_content(body)
    server.send_message(msg)
    server.close()
    

