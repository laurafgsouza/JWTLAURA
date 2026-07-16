from app.extensions import ma
from app.models.service import Service, ServiceOrder

class ServiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Service
        load_instance = False

class ServiceOrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceOrder
        load_instance = False
