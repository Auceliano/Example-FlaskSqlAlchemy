from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Something unique and secret!'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////dbtech.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

db = SQLAlchemy(app)

from TechApp import views, models

from flask_admin import Admin

admin = Admin(app, name='SITE', template_mode='bootstrap3')
from flask_admin.contrib.sqla import ModelView
admin.add_view(ModelView(models.Usuario, db.session))
admin.add_view(ModelView(models.Endereco, db.session))
admin.add_view(ModelView(models.Emprestimo, db.session))
admin.add_view(ModelView(models.Livro, db.session))
admin.add_view(ModelView(models.Sessao, db.session))
