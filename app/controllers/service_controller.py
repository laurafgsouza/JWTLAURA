from app.extensions import db
from app.models.service import Service, ServiceOrder
from app.schemas.service_schema import ServiceSchema, ServiceOrderSchema
from app.utils.response import success_response

service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)
service_order_schema = ServiceOrderSchema()
service_orders_schema = ServiceOrderSchema(many=True)

def listar_servicos():
    servicos = Service.query.all()
    return success_response(services_schema.dump(servicos))

def criar_servico(data):
    dados_validados = service_schema.load(data)
    novo_servico = Service(**dados_validados)
    db.session.add(novo_servico)
    db.session.commit()
    return success_response(service_schema.dump(novo_servico), 201)

def listar_ordens():
    ordens = ServiceOrder.query.all()
    return success_response(service_orders_schema.dump(ordens))

def listar_ordens_por_servico(service_id):
    service = Service.query.get_or_404(service_id)
    return success_response(service_orders_schema.dump(service.ordens))

def criar_ordem(data):
    dados_validados = service_order_schema.load(data)
    nova_ordem = ServiceOrder(**dados_validados)
    db.session.add(nova_ordem)
    db.session.commit()
    return success_response(service_order_schema.dump(nova_ordem), 201)
