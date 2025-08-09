from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Gandalf1234r@localhost/flask_livro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'SaoPaulo123' #alterar depois

db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app.routes import homepage
from app.models import Livro