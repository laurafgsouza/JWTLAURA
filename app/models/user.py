from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, default=False)
    mensagens = db.relationship('Message', backref='usuario', lazy=True)
