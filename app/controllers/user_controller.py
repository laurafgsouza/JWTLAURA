from app.extensions import db
from app.models.user import User
from app.schemas.user_schema import UserSchema
from app.utils.response import success_response
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

user_schema = UserSchema()
users_schema = UserSchema(many=True)


def listar_usuarios():
    usuarios = User.query.all()
    return success_response(users_schema.dump(usuarios))


def criar_usuario(data):
    dados_validados = user_schema.load(data)

    dados_validados["senha"] = generate_password_hash(dados_validados["senha"])
    novo_usuario = User(**dados_validados)

    db.session.add(novo_usuario)
    db.session.commit()

    return success_response(user_schema.dump(novo_usuario), 201)


def atualizar_usuario(id, data):
    usuario = User.query.get_or_404(id)

    dados_validados = user_schema.load(data, partial=True)

    for campo, valor in dados_validados.items():
        setattr(usuario, campo, valor)

    db.session.commit()

    return success_response(user_schema.dump(usuario))


def deletar_usuario(id):
    usuario = User.query.get_or_404(id)

    db.session.delete(usuario)
    db.session.commit()

    return "", 204

def login_usuario(data):
    email = data.get("email")
    senha = data.get("senha")

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.senha, senha):
        token = create_access_token(identity=str(user.id))
        return {"access_token": token}, 200

    return {"msg": "Credenciais inválidas"}, 401
