import mysql.connector

class DisciplinaRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='universidade_np2'
        )
        self.cursor = self.connection.cursor()


    def cadastrar_disciplina(self, disciplina):
        query = "INSERT INTO disciplina_universidade (Nome, Departamento, Codigo, Turno) VALUES (%s, %s, %s, %s)"
        values = (disciplina.nome, disciplina.departamento, disciplina.codigo, disciplina.turno)
        self.cursor.execute(query, values)
        self.connection.commit()
        return True


    def buscar_disciplinas(self):
        query = "SELECT * FROM disciplina_universidade"
        self.cursor.execute(query)
        disciplinas = self.cursor.fetchall()
        return disciplinas


    def buscar_disciplina_por_id(self, id):
        query = "SELECT * FROM disciplina_universidade WHERE id = %s"
        self.cursor.execute(query, (id,))
        disciplina = self.cursor.fetchone()
        return disciplina


    def editar_disciplina(self, id, disciplina):
        if not self.verificar_id_existente(id):
            return None  # Retorna None se o ID não existe
        else:
            query = "UPDATE disciplina_universidade SET Nome = %s, Departamento = %s, Codigo = %s, Turno = %s WHERE id = %s"
            values = (disciplina.nome, disciplina.departamento, disciplina.codigo, disciplina.turno, id)
            self.cursor.execute(query, values)
            self.connection.commit()
            return True

    def verificar_id_existente(self, id):
        query = "SELECT id FROM disciplina_universidade WHERE id = %s"
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        return result is not None

    def excluir_disciplina(self, id):
        if self.disciplina_existe(id):
            query = "DELETE FROM disciplina_universidade WHERE id = %s"
            self.cursor.execute(query, (id,))
            self.connection.commit()
            return True
        else:
            return False


    def disciplina_existe(self, id):
        query = "SELECT COUNT(*) FROM disciplina_universidade WHERE id = %s"
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        return result[0] > 0


    def __del__(self):
        self.cursor.close()
        self.connection.close()
