from model.modelDisciplina import Disciplina
from DTO.dtoDisciplina import DisciplinaDTO
#from DTO.lowDtoAluno import LowAlunoDTO
from repository.repositoryDisciplina import DisciplinaRepository
from flask import Flask, jsonify, request


class DisciplinaService:
    def __init__(self):
        self.repository = DisciplinaRepository()

    def cadastrar_disciplina_service(self):
        data = request.get_json()
        try:
            disciplina_dto = DisciplinaDTO(
                id=None,  # id eh atribuido automaticamente pelo BD
                nome=data['nome'],
                departamento=data['departamento'],
                codigo=data['codigo'],
                turno=data['turno']
            )
            if self.repository.cadastrar_disciplina(disciplina_dto):
                return jsonify({"msg": "Disciplina cadastrado com sucesso"}), 201
        except:
            return jsonify({"msg": "Erro ao cadastrar disciplina"}), 500


# ----------------------------------------//---------------------------------------------

    def buscar_disciplinas_service(self):
        disciplinas = self.repository.buscar_disciplinas()
        todos_disciplinas = [DisciplinaDTO(disciplina[0], disciplina[1], disciplina[2], disciplina[3], disciplina[4]) for disciplina in disciplinas]
        disciplinas_dict = [disciplina.__dict__ for disciplina in todos_disciplinas]
        return jsonify(disciplinas_dict), 200


# ----------------------------------------//---------------------------------------------


    def buscar_disciplina_por_id_service(self, id):
        disciplina = self.repository.buscar_disciplina_por_id(id)
        if disciplina:
            disciplina = DisciplinaDTO(disciplina[0], disciplina[1], disciplina[2], disciplina[3], disciplina[4])
            return jsonify(disciplina.__dict__), 200
        else:
            return jsonify({"error": "Disciplina não encontrado"}), 404


# ----------------------------------------//---------------------------------------------


    def editar_disciplina_service(self, id):
        data = request.get_json()
        disciplina_dto = DisciplinaDTO(None, data['nome'], data['departamento'], data['codigo'], data['turno'])

        if self.repository.editar_disciplina(id, disciplina_dto):
            return jsonify({"msg": "Disciplina editada com sucesso"}), 200
        else:
            return jsonify({"msg": "Erro ao editar disciplina"}), 500


# ----------------------------------------//---------------------------------------------


    def excluir_disciplina_service(self, id):
        if self.repository.excluir_disciplina(id):
            return jsonify({"msg": "Disciplina excluído com sucesso"}), 200
        else:
            return jsonify({"msg": "Disciplina não encontrada"}), 404
