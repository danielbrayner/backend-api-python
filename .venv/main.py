from flask import Flask
from flasgger import Swagger
from controller.controllerAluno import aluno_bp
from controller.controllerDocente import docente_bp
from controller.controllerDisciplina import disciplina_bp


app = Flask(__name__)
swagger = Swagger(app)

# Registra os blueprints
app.register_blueprint(aluno_bp, url_prefix='/aluno')
app.register_blueprint(docente_bp, url_prefix='/docente')
app.register_blueprint(disciplina_bp, url_prefix='/disciplina')


if __name__ == '__main__':
    app.run(debug=True)

