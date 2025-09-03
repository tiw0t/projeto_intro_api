from models import Tarefa
from models import db


class TarefaController:

    @staticmethod
    def get_listar_tarefas():
        return Tarefa.query.all()

    @staticmethod
    def get_listar_tarefas_id(tarefa_id):
        return Tarefa.query.get(tarefa_id)

    @staticmethod
    def criar_tarefa(id, tarefa, concluida):
        pass

    @staticmethod
    def atualizar_tarefa(self, tarefa_id, dados: dict):
        pass

    @staticmethod
    def deletar_tarefas(self, tarefa_id: int):
        pass
