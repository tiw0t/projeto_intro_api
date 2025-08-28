from flask import Blueprint, jsonify, request
from controllers.tarefa_controller import TarefasController

tarefas_dp = Blueprint('tarefas', __name__)

@tarefas_dp.route('/tarefas', methods=['GET'])
def get_listar_tarefas():
    return jsonify([tarefa.to_dict() for tarefa in TarefasController.get_listar_tarefa()])