import mysql.connector


class Conectar():
    def __init__(self):
        self.conexion = mysql.connector.connect(
            user='root', password='', host='localhost', database='u250519348_actividades', port='3306')

    def registrarUsuario(self, userName, edad):
        try:
            cursor = self.conexion.cursor()
            sql = '''INSERT INTO usuarios(userName,edad) VALUES('{}','{}')'''.format(
                userName, edad)
            cursor.execute(sql)
            self.conexion.commit()
            cursor.close()
        except Exception as e:
            print("Error inesperado:", e)

    def actualizarUsuario(self,  userName,  edad):
        try:

            cursor = self.conexion.cursor()
            sql = '''UPDATE usuarios SET userName ='{}', edad = '{}' WHERE userName = '{}' '''.format(userName,
                                                                                                      edad, userName)
            cursor.execute(sql)
            a = cursor.rowcount
            self.conexion.commit()
            cursor.close()
            return a  # retorna 0 o 1
        except Exception as e:
            print("Error inesperado:", e)

    def consultarUsuarios(self, userName, email, edad):
        try:

            cursor = self.conexion.cursor()
            sql = 'SELECT * FROM usuarios'
            cursor.execute(sql)
            usuarios = cursor.fetchall()
            return usuarios
        except Exception as e:
            print("Error inesperado:", e)

    def consultarUsuariosPorUserName(self, userName):
        try:

            cursor = self.conexion.cursor()
            sql = '''SELECT * FROM usuarios WHERE userName='{}' '''.format(
                userName)
            cursor.execute(sql)
            usuario = cursor.fetchall()
            return usuario
        except Exception as e:
            print("Error inesperado:", e)

    def eliminarUsuario(self, email):
        try:

            cursor = self.conexion.cursor()
            sql = '''DELETE FROM usuarios WHERE email = '{}' '''.format(
                email)
            cursor.execute(sql)
            self.conexion.commit()
            cursor.close()
        except Exception as e:
            print("Error inesperado:", e)

    def consultarChat(self, userName, fecha):
        try:
            print(userName)
            cursor = self.conexion.cursor()
            sql = '''SELECT * FROM chats where userName = '{}' AND createdAt = '{}' '''.format(
                userName, fecha)
            cursor.execute(sql)
            chat = cursor.fetchall()
            return chat
        except Exception as e:
            print("Error inesperado:", e)

    def registrarChat(self, userName, chat):
        try:
            cursor = self.conexion.cursor()
            sql = '''INSERT INTO chats(userName,chat) VALUES('{}','{}')'''.format(
                userName, chat)
            cursor.execute(sql)
            self.conexion.commit()
            cursor.close()
        except Exception as e:
            print("Error inesperado:", e)
