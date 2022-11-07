from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route("/")
def index():
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacoes = cotacoes.json()
    cotacao_dolar = str(cotacoes['USDBRL']['bid']).replace('.', ',')
    cotacao_euro = str(cotacoes['EURBRL']['bid']).replace('.', ',')
    cotacao_btc = str(cotacoes['BTCBRL']['bid']).replace('.', ',')
    return render_template('index.html', dolar=cotacao_dolar[:8], euro=cotacao_euro[:8], bitcoin=cotacao_btc[:8])
app.run(port=8080, debug=True)
