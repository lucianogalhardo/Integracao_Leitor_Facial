from flask import Flask, Blueprint, jsonify, request
import json
import os

# Criação da aplicação principal
app = Flask(__name__)

# Definindo o Blueprint e a rota
event = Blueprint('event', __name__)

@event.route('/device_is_alive.fcgi', methods=['POST'])
def device_is_alive():
    print('event.device_is_alive')
    data = request.get_json()  # Captura o JSON da requisição
    print(data)
    print(request.args)


    # Verifica se a chave 'access_logs' existe no JSON recebido
    if 'access_logs' not in data:
        return jsonify({"error": "Campo 'access_logs' não encontrado."}), 400

    # Registra os dados recebidos em um arquivo JSON
    # Lê os dados existentes do arquivo JSON
    existing_logs = []
    if os.path.exists('received_data.json'):
        with open('received_data.json', 'r') as json_file:
            try:
                existing_logs = json.load(json_file)  # Carrega todos os logs como uma lista
            except json.JSONDecodeError:
                return jsonify({"error": "O arquivo JSON está corrompido."}), 500

    # Adiciona o novo log à lista existente, evitando duplicatas
    new_log = data['access_logs']
    
    # Verifica se o novo log já está presente
    if new_log not in existing_logs:
        existing_logs.append(new_log)  # Adiciona o novo log à lista existente
        with open('received_data.json', 'w') as json_file:
            json.dump(existing_logs, json_file, indent=4)  # Grava com indentação
    else:
        print("Log já existente. Não adicionando novamente.")

    # Retorna o campo 'access_logs' do JSON recebido na requisição
    return jsonify(
        access_logs=data.get('access_logs')
    )

@event.route('/get_access_logs', methods=['GET'])
def get_access_logs():
    # Lê os dados do arquivo JSON
    logs = []
    if os.path.exists('received_data.json'):
        with open('received_data.json', 'r') as json_file:
            try:
                logs = json.load(json_file)  # Carrega todos os logs como uma lista
            except json.JSONDecodeError:
                return jsonify({"error": "O arquivo JSON está corrompido."}), 500

    # Se logs estiver vazio, retorna uma mensagem apropriada
    if not logs:
        return jsonify({"message": "Nenhum log encontrado."}), 404

    # Retorna os dados lidos como JSON
    return jsonify(logs)

# Registrando o Blueprint na aplicação principal
app.register_blueprint(event)

# Iniciando o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)  # debug=True é opcional e exibe erros detalhados no console
