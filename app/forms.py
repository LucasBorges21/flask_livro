from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import ValidationError, DataRequired

from app import db
from app.models import Livro

class LivroForm(FlaskForm):
    titulo= StringField('Título', validators=[DataRequired()])
    autor= StringField('Autor', validators=[DataRequired()])
    categoria= StringField('Categoria', validators=[DataRequired()])
    editora= StringField('Editora', validators=[DataRequired()])
    preco= DecimalField('Preço', validators=[DataRequired()])
    ano_publicacao= StringField('Ano de Publicação', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self):
        livro = Livro (
            titulo = self.titulo.data,
            autor = self.autor.data,
            categoria = self.categoria.data,
            editora = self.editora.data,
            preco = self.preco.data,
            ano_publicacao = self.ano_publicacao.data
        )

        db.session.add(livro)
        db.session.commit()