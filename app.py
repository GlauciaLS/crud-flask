from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/youtube'

db = SQLAlchemy(app)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))

    def to_json(self):
        return {"id": self.id, "nome": self.nome, "email": self.email}


@app.route("/usuarios", methods=["GET"])
def seleciona_usuarios():
    usuarios_objetos = Usuario.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]

    return gera_response(200, "usuarios", usuarios_json, "ok")


@app.route("/usuario/<id>", methods=["GET"])
def seleciona_usuario(id):
    usuario_objeto = encontra_usuario(id)
    usuario_json = usuario_objeto.to_json()

    return gera_response(200, "usuario", usuario_json)


@app.route("/usuario", methods=["POST"])
def cria_usuario():
    body = request.get_json()

    try:
        usuario = Usuario(nome=body["nome"], email=body["email"])
        db.session.add(usuario)
        db.session.commit()
        return gera_response(201, "usuario", usuario.to_json(), "Criado com sucesso")

    except Exception as e:
        print(e)
        return gera_response(400, "usuario", {}, "Erro ao cadastrar")


@app.route("/usuario/<id>", methods=["PUT"])
def atualiza_usuario(id):
    usuario_objeto = encontra_usuario(id)
    body = request.get_json()

    try:
        if 'nome' in body:
            usuario_objeto.nome = body['nome']
        if 'email' in body:
            usuario_objeto.email = body['email']

        db.session.add(usuario_objeto)
        db.session.commit()
        return gera_response(200, "usuario", usuario_objeto.to_json(), "Atualizado com sucesso")

    except Exception as e:
        print(e)
        return gera_response(400, "usuario", {}, "Erro ao atualizar")


def encontra_usuario(id):
    return Usuario.query.filter_by(id=id).first()


def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {nome_do_conteudo: conteudo}

    if mensagem:
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")


app.run()