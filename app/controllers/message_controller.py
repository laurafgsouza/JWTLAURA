from app.extensions import db
from app.models.message import Message
from app.models.user import User
from app.schemas.message_schema import MessageSchema
from app.utils.response import success_response

message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)

def listar_mensagens():
    mensagens = Message.query.all()
    return success_response(messages_schema.dump(mensagens))

def listar_mensagens_por_usuario(user_id):
    user = User.query.get_or_404(user_id)
    return success_response(messages_schema.dump(user.mensagens))

def criar_mensagem(data):
    dados_validados = message_schema.load(data)
    nova_mensagem = Message(**dados_validados)
    db.session.add(nova_mensagem)
    db.session.commit()
    return success_response(message_schema.dump(nova_mensagem), 201)

def atualizar_mensagem(id, data):
    mensagem = Message.query.get_or_404(id)
    dados_validados = message_schema.load(data, partial=True)
    for campo, valor in dados_validados.items():
        setattr(mensagem, campo, valor)
    db.session.commit()
    return success_response(message_schema.dump(mensagem))

def deletar_mensagem(id):
    mensagem = Message.query.get_or_404(id)
    db.session.delete(mensagem)
    db.session.commit()
    return "", 204
