import mysql.connector

class AlunoRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='universidade_np2'
        )
        self.cursor = self.connection.cursor()


    def cadastrar_aluno(self, aluno):
        query = "INSERT INTO aluno_universidade (Nome, Matricula, Email, DataNascimento) VALUES (%s, %s, %s, %s)"
        values = (aluno.nome, aluno.matricula, aluno.email, aluno.data_nascimento)
        self.cursor.execute(query, values)
        self.connection.commit()
        return True


    def buscar_alunos(self):
        query = "SELECT * FROM aluno_universidade"
        self.cursor.execute(query)
        alunos = self.cursor.fetchall()
        return alunos


    def buscar_aluno_por_id(self, id):
        query = "SELECT * FROM aluno_universidade WHERE id = %s"
        self.cursor.execute(query, (id,))
        aluno = self.cursor.fetchone()
        #print(aluno)
        return aluno


    def editar_aluno(self, id, aluno):
        if not self.verificar_id_existente(id):
            return None  # Retorna None se o ID não existe
        else:
            query = "UPDATE aluno_universidade SET Nome = %s, Matricula = %s, Email = %s, DataNascimento = %s WHERE id = %s"
            values = (aluno.nome, aluno.matricula, aluno.email, aluno.data_nascimento, id)
            self.cursor.execute(query, values)
            self.connection.commit()
            return True

    def verificar_id_existente(self, id):
        query = "SELECT id FROM aluno_universidade WHERE id = %s"
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        return result is not None

    def excluir_aluno(self, id):
        if self.aluno_existe(id):
            query = "DELETE FROM aluno_universidade WHERE id = %s"
            self.cursor.execute(query, (id,))
            self.connection.commit()
            return True
        else:
            return False


    def aluno_existe(self, id):
        query = "SELECT COUNT(*) FROM aluno_universidade WHERE id = %s"
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        return result[0] > 0


    def __del__(self):
        self.cursor.close()
        self.connection.close()
