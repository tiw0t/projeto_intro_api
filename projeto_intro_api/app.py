from flask import Flask, jsonify

app = Flask(__name__)

def hello_world():
    return jsonify({'message': 'Olá, Mundo! Bem-vindo à API Flask. '})