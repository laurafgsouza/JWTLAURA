from app.extensions import ma
from app.models.message import Message

class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message
        load_instance = False
