from flask import Blueprint, Flask, jsonify, request
from DTO.dtoDocente import DocenteDTO
from DTO.lowDtoDocente import LowDocenteDTO
from service.serviceDocente import DocenteService
from flasgger import Swagger, swag_from


app = Flask(__name__)
swagger = Swagger(app)
docente_service = DocenteService()
docente_bp = Blueprint('docente_bp', __name__)



@docente_bp.route('/cadastrar_docente', methods=['POST'])
@swag_from({
    'tags': ['Docentes'],
    'description': 'Endpoint para cadastrar um novo docente.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'matricula': {'type': 'string'},
                    'email': {'type': 'string'},
                    'data_nascimento': {'type': 'string', 'format': 'date'}
                },
                'required': ['nome', 'matricula', 'email', 'data_nascimento']
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Sucesso',
            'examples': {
                'application/json': {"msg": "Docente cadastrado com sucesso"}
            }
        },
        '500': {
            'description': 'Error',
            'examples': {
                'application/json': {"msg": "Erro ao cadastrar docente"}
            }
        }
    }
})
def cadastrar_docente():
    return docente_service.cadastrar_docente_service()


#----------------------------------------//---------------------------------------------

@docente_bp.route('/buscar_todos_docentes', methods=['GET'])
@swag_from({
    'tags': ['Docentes'],
    'responses': {
        '200': {
            'description': 'Lista de todos os docentes',
            'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Docente'}}}}
        }
    }
})
def buscar_docentes():
    return docente_service.buscar_docentes_service()


#----------------------------------------//---------------------------------------------


@docente_bp.route('/buscar_docente_por_id/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Docentes'],
    'description': 'Endpoint para buscar docente pelo ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do docente a ser buscado'
        }
    ],
    'responses': {
        '200': {
            'description': 'Sucesso',
            'content': {'application/json': {'schema': {'$ref': '#/definitions/Docente'}}}
        },
        '404': {
            'description': 'Docente não encontrado',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def buscar_docente_por_id(id):
    return docente_service.buscar_docente_por_id_service(id)


#----------------------------------------//---------------------------------------------


@docente_bp.route('/editar_docente/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Docentes'],
    'description': 'Endpoint para editar um docente passando seu ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do docente a ser editado'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Informações do docente a serem atualizadas',
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'matricula': {'type': 'string'},
                    'email': {'type': 'string'},
                    'data_nascimento': {'type': 'string', 'format': 'date'}
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': '"msg": "Docente editado com sucesso"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        },
        '500': {
            'description': '"msg": "Erro ao editar docente"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def editar_docente(id):
    return docente_service.editar_docente_service(id)


#----------------------------------------//---------------------------------------------



@docente_bp.route('/deletar_docente/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Docentes'],
    'description': 'Endpoint para deletar um docente passando seu ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do docente a ser excluído'
        }
    ],
    'responses': {
        '200': {
            'description': '"msg": "Docente excluído com sucesso"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        },
        '404': {
            'description': '"msg": "Docente não encontrado"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def excluir_docente(id):
    return docente_service.excluir_docente_service(id)






