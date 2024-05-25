from model.modelDocente import Docente
from DTO.dtoDocente import DocenteDTO
from DTO.lowDtoDocente import LowDocenteDTO
from repository.repositoryDocente import DocenteRepository
from flask import Flask, jsonify, request


class DocenteService:
    def __init__(self):
        self.repository = DocenteRepository()

    def cadastrar_docente_service(self):
        data = request.get_json()
        try:
            docente_dto = DocenteDTO(
                id=None,  # id eh atribuido automaticamente pelo BD
                nome=data['nome'],
                matricula=data['matricula'],
                email=data['email'],
                data_nascimento=data['data_nascimento']
            )
            if self.repository.cadastrar_docente(docente_dto):
                return jsonify({"msg": "Docente cadastrado com sucesso"}), 201
        except:
            return jsonify({"msg": "Erro ao cadastrar docente"}), 500


# ----------------------------------------//---------------------------------------------

    def buscar_docentes_service(self):
        docentes = self.repository.buscar_docentes()
        todos_docentes = [DocenteDTO(docente[0], docente[1], docente[2], docente[3], docente[4]) for docente in docentes]
        docentes_dict = [docente.__dict__ for docente in todos_docentes]
        return jsonify(docentes_dict), 200


# ----------------------------------------//---------------------------------------------


    def buscar_docente_por_id_service(self, id):
        docente = self.repository.buscar_docente_por_id(id)
        if docente:
            docente = DocenteDTO(docente[0], docente[1], docente[2], docente[3], docente[4])
            return jsonify(docente.__dict__), 200
        else:
            return jsonify({"error": "Docente não encontrado"}), 404


# ----------------------------------------//---------------------------------------------


    def editar_docente_service(self, id):
        data = request.get_json()
        docente_dto = DocenteDTO(None, data['nome'], data['matricula'], data['email'], data['data_nascimento'])

        if self.repository.editar_docente(id, docente_dto):
            return jsonify({"msg": "Docente editado com sucesso"}), 200
        else:
            return jsonify({"msg": "Erro ao editar docente"}), 500


# ----------------------------------------//---------------------------------------------


    def excluir_docente_service(self, id):
        if self.repository.excluir_docente(id):
            return jsonify({"msg": "Docente excluído com sucesso"}), 200
        else:
            return jsonify({"msg": "Docente não encontrado"}), 404
