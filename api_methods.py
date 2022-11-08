from flask import Flask, jsonify, request

import dbSettings as db

# cria uma instância da aplicação Flask
app = Flask(__name__) 


@app.route('/') # rota raíz da aplicação
def homePage(): # função que retorna a página inicial da aplicação
  return 'API online' # retorna a página inicial da aplicação

# rota para selecionar dados
@app.route('/select', methods=['GET'])  
def select(): 
    return jsonify(db.select_temp()) # retorna os dados do banco de dados

# inserir dados
@app.route('/insert', methods=['POST'])
def insert():
    data = request.get_json()
    weather = db.weather_md(data['temperature'], data['humidity'], data['dewpoint'], data['pressure'], data['speed'], data['direction'], data['datetime'])
    db.insert(weather)
    return jsonify({'message': 'Dados inseridos com sucesso!'})
    

app.run(host='0.0.0.0') # inicia a aplicação Flask
