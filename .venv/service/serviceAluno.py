from model.modelAluno import Aluno
from DTO.dtoAluno import AlunoDTO
from DTO.lowDtoAluno import LowAlunoDTO
from repository.repositoryAluno import AlunoRepository
from flask import Flask, jsonify, request


class AlunoService:
    def __init__(self):
        self.repository = AlunoRepository()

    def cadastrar_aluno_service(self):
        data = request.get_json()
        try:
            aluno_dto = AlunoDTO(
                id=None,  # id eh atribuido automaticamente pelo BD
                nome=data['nome'],
                matricula=data['matricula'],
                email=data['email'],
                data_nascimento=data['data_nascimento']
            )
            if self.repository.cadastrar_aluno(aluno_dto):
                return jsonify({"msg": "Aluno cadastrado com sucesso"}), 201
        except:
            return jsonify({"msg": "Erro ao cadastrar aluno"}), 500


# ----------------------------------------//---------------------------------------------

    def buscar_alunos_service(self):
        alunos = self.repository.buscar_alunos()
        todos_alunos = [AlunoDTO(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4]) for aluno in alunos]
        alunos_dict = [aluno.__dict__ for aluno in todos_alunos]
        return jsonify(alunos_dict), 200


# ----------------------------------------//---------------------------------------------


    def buscar_aluno_por_id_service(self, id):
        aluno = self.repository.buscar_aluno_por_id(id)
        if aluno:
            aluno = AlunoDTO(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4])
            return jsonify(aluno.__dict__), 200
        else:
            return jsonify({"error": "Aluno não encontrado"}), 404


# ----------------------------------------//---------------------------------------------


    def editar_aluno_service(self, id):
        data = request.get_json()
        aluno_dto = AlunoDTO(None, data['nome'], data['matricula'], data['email'], data['data_nascimento'])

        if self.repository.editar_aluno(id, aluno_dto):
            return jsonify({"msg": "Aluno editado com sucesso"}), 200
        else:
            return jsonify({"msg": "Erro ao editar aluno"}), 500


# ----------------------------------------//---------------------------------------------


    def excluir_aluno_service(self, id):
        if self.repository.excluir_aluno(id):
            return jsonify({"msg": "Aluno excluído com sucesso"}), 200
        else:
            return jsonify({"msg": "Aluno não encontrado"}), 404
