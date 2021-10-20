# Fazer requisições
import requests

# Para criar uma página na Web
from flask import Flask
print('Qual é o seu cep? \n')
cep_client = input(str())

# Retirando espaços no começo e no fim da string
cep_client = cep_client.strip()

if len(cep_client) == 9:
    cep_client = cep_client.replace('-', '')

# Retirar tudo que não for númer dese CEP.
# REGEXP

r = requests.get(f'https://viacep.com.br/ws/{cep_client}/json/')
r = r.json()

app = Flask(__name__)


@app.route('/')
def return_cep():
    return r

# Usar isso aqui no Shell
#set FLASK_APP=class_api_basic.py
#$env:FLASK_APP = "class_api_basic.py"
#flask run
