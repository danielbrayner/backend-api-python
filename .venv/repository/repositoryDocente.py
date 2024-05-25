import mysql.connector

class DocenteRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='universidade_np2'
        )
        self.cursor = self.connection.cursor()


    def cadastrar_docente(self, docente):
        query = "INSERT INTO docente_universidade (Nome, Matricula, Email, DataNascimento) VALUES (%s, %s, %s, %s)"
        values = (docente.nome, docente.matricula, docente.email, docente.data_nascimento)
        self.cursor.execute(query, values)
        self.connection.commit()
        return True


    def buscar_docentes(self):
        query = "SELECT * FROM docente_universidade"
        self.cursor.execute(query)
        docentes = self.cursor.fetchall()
        return docentes


    def buscar_docente_por_id(self, id):
        query = "SELECT * FROM docente_universidade WHERE id = %s"
        self.cursor.execute(query, (id,))
        docente = self.cursor.fetchone()
        return docente


    def editar_docente(self, id, docente):
        if not self.verificar_id_existente(id):
            return None  # Retorna None se o ID não existe
        else:
            query = "UPDATE docente_universidade SET Nome = %s, Matricula = %s, Email = %s, DataNascimento = %s WHERE id = %s"
            values = (docente.nome, docente.matricula, docente.email, docente.data_nascimento, id)
            self.cursor.execute(query, values)
            self.connection.commit()
            return True

    def verificar_id_existente(self, id):
        query = "SELECT id FROM docente_universidade WHERE id = %s"
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        return result is not None

    def excluir_docente(self, id):
        if self.docente_existe(id):
            query = "DELETE FROM docente_universidade WHERE id = %s"
            self.cursor.execute(query, (id,))
            self.connection.commit()
            return True
        else:
            return False


    def docente_existe(self, id):
        query = "SELECT COUNT(*) FROM docente_universidade WHERE id = %s"
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchone()
        return result[0] > 0


    def __del__(self):
        self.cursor.close()
        self.connection.close()
