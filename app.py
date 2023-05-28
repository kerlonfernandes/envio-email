import os 
import smtplib
from email.message import EmailMessage
from secret import senha

#Configura email, senha
EMAIL_ADDRESS = '@gmail.com'
EMAIL_PASSWORD = senha

#Criar um e-mail
msg = EmailMessage()
msg['Subject'] = 'Olá'
msg['From'] = @gmail.com" 
msg['To'] = ['@gmail.com']
msg.set_content('Olá, este é um exemplo de email')


#Enviar email
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)

    print("Email Enviado!")
