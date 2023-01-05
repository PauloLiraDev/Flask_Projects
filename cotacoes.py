from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route("/")

def index():
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacoes = cotacoes.json()
    dolar = str(cotacoes['USDBRL']['bid']).replace('.', ',')
    euro = str(cotacoes['EURBRL']['bid']).replace('.', ',')
    bitcoin = str(cotacoes['BTCBRL']['bid'])
    return render_template('index.html', dolar=dolar, euro=euro, bitcoin=bitcoin)


app.run(host='0.0.0.0', port=8080, debug=True)
