from models import Tarefa
from models import db


class TarefaController:

    @staticmethod
    def get_listar_tarefas():
        return Tarefa.query.all()

    def get_listar_tarefas_id(tarefa_id):
        pass

    def criar_tarefa(id, tarefa, concluida):
        pass

    def atualizar_tarefa(self, tarefa_id, dados: dict):
        pass

    def deletar_tarefas(self, tarefa_id: int):
        pass
