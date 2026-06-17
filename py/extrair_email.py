import re
import pandas as pd

from docx import Document #Importa a biblioteca para manipular o docs
caminho_arquivo = "documentos_word/IF_AC_MS_AP.docx" #cria variável do caminho do arquivo
documento = Document(caminho_arquivo) #Cria um objeto documento a partir do caminho do arquivo

texto_completo = ""
for paragrafo in documento.paragraphs:
    texto_completo += paragrafo.text + "\n"

#print(texto_completo)
padrao_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails_encontrados = re.findall(padrao_email, texto_completo)
#print(emails_encontrados)

emails_unicos = set(emails_encontrados)
#print(len(emails_unicos))

dominios_estados = {
    "ifap.edu.br":"AP",
    "ifms.edu.br":"MS",
    "ifac.edu.br":"AC"
}

correcoes_dominio = {
    "ifms.edu": "ifms.edu.br",
    "ifac.edu": "ifac.edu.br",
    "ifap.edu": "ifap.edu.br"
}

suspeitos = []
validos = []

for email in emails_unicos:
    dominio = email.split("@")[1]

    if dominio in correcoes_dominio:
        dominio = correcoes_dominio[dominio]

    if dominio in dominios_estados: 
        estado = dominios_estados[dominio]
        validos.append((email, estado))
        print(email, estado)
    else: 
        suspeitos.append(email)
        print("SUSPEITO:", email)
#print(len(suspeitos))
#print(len(validos))

tabela = pd.DataFrame(validos,columns=["email", "estado"])
print(tabela)
tabela.to_csv("planilhas/emails_validos.csv", index=False)

tabela_suspeitos = pd.DataFrame(suspeitos, columns=["email"])
print(tabela_suspeitos)
tabela_suspeitos.to_csv("planilhas/emails_suspeitos.csv", index=False)