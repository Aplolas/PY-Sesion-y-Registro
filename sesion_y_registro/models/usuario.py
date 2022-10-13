from sesion_y_registro.config.mysqlconnection import connectToMySQL
from flask import flash, request
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Usuario:
    db="sesion_y_registro"

    def __init__ (self,data):
        self.id = data['id']
        self.nombre = data['first_name']
        self.apellido = data['last_name']
        self.email = data['email']
        self.password = data['password']


    @classmethod
    def all_users(cls):
        query = "SELECT * FROM user;"
        resultado =  connectToMySQL(cls.db).query_db(query)
        registro_usuarios =[]
        for i in resultado:
            registro_usuarios.append(cls(i))
        return registro_usuarios
    

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM user WHERE id=%(identificador)s;"
        resultado = connectToMySQL(cls.db).query_db(query, data )
        return cls(resultado[0])


    @classmethod
    def obtener_x_mail(cls,data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        
        if len(result) < 1:
            return False
        return cls(result[0])


    @classmethod
    def save(cls,data):
        query = "INSERT INTO user (first_name,last_name,email,password) VALUES (%(nombre)s,%(apellido)s,%(email)s,%(password)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    

    @staticmethod
    def validate(registro):
        correo = {
            'email':registro['email']
        }

        is_valid = True
        if len(registro['nombre']) < 4:
            flash("Nom : au moins 2 caractères")
            is_valid = False
        if len(registro['apellido']) < 4:
            flash("Nom: au mois 2 caractères")
            is_valid = False
        if not EMAIL_REGEX.match(correo['email']): 
            flash("Adresse e-mail non valide")
            is_valid = False
        elif Usuario.obtener_x_mail(correo):
            flash("Adresse e-mail existante")
            is_valid = False
        if len(registro['password']) < 8:
            flash("Mot de passe non sécurisé : au moins 8 caractères")
            is_valid = False
        if registro['password'] != registro['password_confirm']:
            flash("Les mots de passe ne correspondent pas")
            is_valid = False
        return is_valid