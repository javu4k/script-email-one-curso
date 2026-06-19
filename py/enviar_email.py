import smtplib
import pandas as pd
import time 

from config import EMAIL, SENHA
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

tabela = pd.read_csv("planilhas/teste.csv")

servidor = smtplib.SMTP_SSL("smtp.gmail.com", 465)
servidor.login(EMAIL, SENHA)
contador = 0
#deixar isso aqui em cima sempre

try:
    with open("log.txt", "r") as arquivo_log:
        emails_log = arquivo_log.read().splitlines()
except:
    emails_log = []

#essa parte tá enviando o email, então pode ficar por ultimo
for indice, linha in tabela.iterrows():
    if linha["email"] in emails_log:
        print(f'Email para {linha["email"]} já foi enviado anteriormente. Pulando')
        continue

    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = linha['email']
    msg['Subject'] = "Testeeeeee"
    corpo = "email de testeee, oremos, omnia in bonum"
    msg.attach(MIMEText(corpo,'plain'))

    try:
        servidor.sendmail(EMAIL, linha['email'], msg.as_string())

        with open("log.txt", "a") as arquivo_log:
                arquivo_log.write(linha["email"] + "\n")
        print(f"Email enviado para: {linha['email']}")

    except Exception as e:
        print(f"Erro ao enviar para {linha['email']}: {e}")
        with open("planilhas/erros.csv", "a") as arquivo_erros:
            arquivo_erros.write(f"{linha['email']};{str(e)}\n")

    contador +=1

    if contador %480 ==0:
        print("480 emails enviados. Pausa de 1h")
        time.sleep(3600)  # 1hora

servidor.quit()
print("Emails enviados com sucesso!")