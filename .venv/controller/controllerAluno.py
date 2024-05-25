from flask import Blueprint, Flask, jsonify, request
from DTO.dtoAluno import AlunoDTO
from DTO.lowDtoAluno import LowAlunoDTO
from service.serviceAluno import AlunoService
from flasgger import Swagger, swag_from


app = Flask(__name__)
swagger = Swagger(app)
aluno_service = AlunoService()
aluno_bp = Blueprint('aluno_bp', __name__)



@aluno_bp.route('/cadastrar_alunos', methods=['POST'])
@swag_from({
    'tags': ['Alunos'],
    'description': 'Endpoint para cadastrar um novo aluno.',
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
                'application/json': {"msg": "Aluno cadastrado com sucesso"}
            }
        },
        '500': {
            'description': 'Error',
            'examples': {
                'application/json': {"msg": "Erro ao cadastrar aluno"}
            }
        }
    }
})
def cadastrar_aluno():
    return aluno_service.cadastrar_aluno_service()


#----------------------------------------//---------------------------------------------

@aluno_bp.route('/buscar_todos_alunos', methods=['GET'])
@swag_from({
    'tags': ['Alunos'],
    'responses': {
        '200': {
            'description': 'Lista de todos os alunos',
            'content': {'application/json': {'schema': {'type': 'array', 'items': {'$ref': '#/components/schemas/Aluno'}}}}
        }
    }
})
def buscar_alunos():
    return aluno_service.buscar_alunos_service()


#----------------------------------------//---------------------------------------------


@aluno_bp.route('/buscar_aluno_por_id/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Alunos'],
    'description': 'Endpoint para buscar aluno pelo ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do aluno a ser buscado'
        }
    ],
    'responses': {
        '200': {
            'description': 'Sucesso',
            'content': {'application/json': {'schema': {'$ref': '#/definitions/Aluno'}}}
        },
        '404': {
            'description': 'Aluno não encontrado',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def buscar_aluno_por_id(id):
    return aluno_service.buscar_aluno_por_id_service(id)


#----------------------------------------//---------------------------------------------


@aluno_bp.route('/editar_aluno/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Alunos'],
    'description': 'Endpoint para editar um aluno passando seu ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do aluno a ser editado'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Informações do aluno a serem atualizadas',
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
            'description': '"msg": "Aluno editado com sucesso"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        },
        '500': {
            'description': '"msg": "Erro ao editar aluno"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def editar_aluno(id):
    return aluno_service.editar_aluno_service(id)


#----------------------------------------//---------------------------------------------



@aluno_bp.route('/deletar_aluno/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Alunos'],
    'description': 'Endpoint para deletar um aluno passando seu ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do aluno a ser excluído'
        }
    ],
    'responses': {
        '200': {
            'description': '"msg": "Aluno excluído com sucesso"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        },
        '404': {
            'description': '"msg": "Aluno não encontrado"',
            'content': {'application/json': {'schema': {'type': 'string'}}}
        }
    }
})
def excluir_aluno(id):
    return aluno_service.excluir_aluno_service(id)






