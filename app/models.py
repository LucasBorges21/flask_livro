from app import db

class Livro(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    titulo= db.Column(db.String(80), nullable=False)
    autor= db.Column(db.String(50), nullable=False)
    categoria= db.Column(db.String(30), nullable=True)
    editora= db.Column(db.String(40), nullable=True)
    preco= db.Column(db.Numeric(10, 2), nullable=False)
    ano_publicacao= db.Column(db.String(4), nullable=True)