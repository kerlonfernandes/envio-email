import os 
import smtplib
from email.message import EmailMessage
from secret import senha

#Configura email, senha
EMAIL_ADDRESS = 'zzmids1@gmail.com'
EMAIL_PASSWORD = senha

#Criar um e-mail
msg = EmailMessage()
msg['Subject'] = 'Olá'
msg['From'] = "zzmids1@gmail.com" 
msg['To'] = ['andrep16082004@gmail.com', 'kerlon1221@gmail.com', 'weldsakira@gmail.com', 'batatrap@gmail.com']
msg.set_content('olá, Amo vocês')


#Enviar email
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)

    print("Email Enviado!")