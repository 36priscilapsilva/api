from flask import Flask, request, jsonify

app = Flask(__name__)
dados = []

@app.route('/')
def home():
    return "🚀 Bem-vinda à API da Priscila! Use o endpoint /itens para interagir com a API."

@app.route('/itens', methods=['GET'])
def listar_itens():
    return jsonify(dados)

@app.route('/itens', methods=['POST'])
def adicionar_item():
    item = request.json
    dados.append(item)
    return jsonify(item), 201

app.run(host='0.0.0.0', port=8000)

