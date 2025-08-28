from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/ola', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Olá, Mundo! Bem-vindo à API Flask. '})


def get_tarefas():
    tarefas = [
        {'id': 1, 'titulo': 'Estudar Flask', 'concluida': False},
        {'id': 2, 'titulo': 'Ler mais sobre programação', 'concluida': False},
        {'id': 3, 'titulo': 'Testar endpoint', 'concluida': False}
    ]
    return jsonify({'tarefas': tarefas})

if __name__ == '__main__':
    app.run(debug=True)