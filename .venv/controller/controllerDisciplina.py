from flask import Blueprint, Flask, jsonify, request
from DTO.dtoDisciplina import DisciplinaDTO
#from DTO.lowDtoAluno import LowAlunoDTO
from service.serviceDisciplina import DisciplinaService
from flasgger import Swagger, swag_from


app = Flask(__name__)
swagger = Swagger(app)
disciplina_service = DisciplinaService()
disciplina_bp = Blueprint('disciplina_bp', __name__)



@disciplina_bp.route('/cadastrar_disciplina', methods=['POST'])
@swag_from({
    'tags': ['Disciplinas'],
    'description': 'Endpoint para cadastrar um novo disciplina.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'departamento': {'type': 'string'},
                    'codigo': {'type': 'string'},
                    'turno': {'type': 'string', 'format': 'string'}
                },
                'required': ['nome', 'departamento', 'codigo', 'turno']
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Sucesso',
            'examples': {
                'application/json': {"msg": "Disciplina cadastrado com sucesso"}
            }
        },
        '500': {
            'description': 'Error',
            'examples': {
                'application/json': {"msg": "Erro ao cadastrar disciplina"}
            }
        }
    }
})
def cadastrar_disciplina():
    return disciplina_service.cadastrar_disciplina_service()


#----------------------------------------//---------------------------------------------

@disciplina_bp.route('/buscar_todas_disciplinas', methods=['GET'])
@swag_from({
    'tags': ['Disciplinas'],
    'responses': {
        '200': {
            'description': 'Lista de todos os disciplinas',
            'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Disciplina'}}}}
        }
    }
})
def buscar_disciplinas():
    return disciplina_service.buscar_disciplinas_service()


#----------------------------------------//---------------------------------------------


@disciplina_bp.route('/buscar_disciplina_por_id/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Disciplinas'],
    'description': 'Endpoint para buscar disciplina pelo ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do disciplina a ser buscado'
        }
    ],
    'responses': {
        '200': {
            'description': 'Sucesso',
            'content': {'application/json': {'schema': {'$ref': '#/definitions/Disciplina'}}}
        },
        '404': {
            'description': 'Disciplina não encontrada',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def buscar_disciplina_por_id(id):
    return disciplina_service.buscar_disciplina_por_id_service(id)


#----------------------------------------//---------------------------------------------


@disciplina_bp.route('/editar_disciplina/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Disciplinas'],
    'description': 'Endpoint para editar uma disciplina passando seu ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da disciplina a ser editada'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Informações da disciplina a serem atualizadas',
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'departamento': {'type': 'string'},
                    'codigo': {'type': 'string'},
                    'turno': {'type': 'string', 'format': 'date'}
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': '"msg": "Disciplina editado com sucesso"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        },
        '500': {
            'description': '"msg": "Erro ao editar disciplina"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def editar_disciplina(id):
    return disciplina_service.editar_disciplina_service(id)


#----------------------------------------//---------------------------------------------



@disciplina_bp.route('/deletar_disciplina/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Disciplinas'],
    'description': 'Endpoint para deletar uma disciplina passando seu ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do disciplina a ser excluído'
        }
    ],
    'responses': {
        '200': {
            'description': '"msg": "Disciplina excluído com sucesso"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        },
        '404': {
            'description': '"msg": "Disciplina não encontrado"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def excluir_disciplina(id):
    return disciplina_service.excluir_disciplina_service(id)






