import smtplib
from config import EMAIL, SENHA
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

servidor = smtplib.SMTP_SSL("smtp.gmail.com", 465)
servidor.login(EMAIL, SENHA)

msg = MIMEMultipart()

msg['From'] = EMAIL
msg['To'] = EMAIL
msg['Subject'] = "Testeeeeee"

corpo = "email de testeee, oremos, omnia in bonum"
msg.attach(MIMEText(corpo,'plain'))

servidor.sendmail(EMAIL, EMAIL, msg.as_string())
servidor.quit()
print("Email enviado com sucesso!")