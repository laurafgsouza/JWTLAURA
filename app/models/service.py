from app.extensions import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    preco_base = db.Column(db.Float, nullable=False)
    ordens = db.relationship('ServiceOrder', backref='servico', lazy=True)

class ServiceOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    servico_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    data = db.Column(db.DateTime, default=db.func.now())
    status = db.Column(db.String(50), default='pendente')
