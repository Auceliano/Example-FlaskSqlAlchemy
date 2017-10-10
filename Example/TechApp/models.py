from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from TechApp import db

class Usuario(db.Model):
    """Entidade Usuário"""
    id = db.Column(
        db.Integer,
        primary_key = True)

    nome = db.Column(db.String(100))

    telefone = db.Column(db.String(20))

    email = db.Column(db.String(50), unique = True)

    senha = db.Column(db.String(100))

    tipo = db.Column(db.String(1))

    id_endereco = db.Column(
            db.Integer,
            db.ForeignKey('endereco.id'))

    endereco = db.relationship(
            'Endereco',
            backref='usuario',
            uselist=False)
    
    emprestimos = db.relationship(
            'Emprestimo',
            backref='usuario',
            lazy='dynamic')

    #Contrutor recebe os atributos nome, telefone e email.
    def __init__(self, nome, telefone, email, senha, tipo):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.tipo = tipo
        #self.id_endereco = id_endereco


class Endereco(db.Model):
    """Entidade Endereço Do Usuário"""
    id = db.Column(
        db.Integer,
        primary_key=True)

    cep = db.Column(db.String(10))

    cidade = db.Column(db.String(30))

    rua = db.Column(db.String(100))

    def __init__(self, cep, cidade, rua):
        self.cep = cep
        self.cidade = cidade
        self.rua = rua
    def __repr__(self):
        return '{}, {} ({})'.format(self.rua, self.cidade, self.cep)


livro_emprestimo = db.Table('livro_emprestimo',
    db.Column('id_livro', db.Integer, db.ForeignKey('livro.id')),
    db.Column('id_emprestimo', db.Integer, db.ForeignKey('emprestimo.id'))
)

class Emprestimo(db.Model):
    """Entidade Empréstimo"""
    id = db.Column(db.Integer, primary_key=True)
    data_emprestimo = db.Column(db.DateTime)
    data_devolucao = db.Column(db.DateTime)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    livros = db.relationship(
        'Livro',
        secondary=livro_emprestimo,
        backref=db.backref(
        'emprestimo',
        lazy='dynamic'))
    
    def __init__(self, data_emprestimo, data_devolucao):
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
    def __repr__(self):
        return '{} ({})'.format(self.data_emprestimo, self.id_usuario)

class Livro(db.Model):
    """Entidade Livro"""
    id = db.Column(
        db.Integer,
        primary_key=True)

    titulo = db.Column(db.String(100))

    autor = db.Column(db.String(100))

    emprestimos = db.relationship(
        'Emprestimo',
        secondary=livro_emprestimo,
        backref=db.backref(
        'livro',
        lazy='dynamic'))

    sessao_id = db.Column(db.Integer, db.ForeignKey('sessao.id'))

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def __repr__(self):
        return '{} ({})'.format(self.titulo, self.autor)

class Sessao(db.Model):
    """Entidade Sessão"""
    id = db.Column(
        db.Integer,
        primary_key=True)

    localizacao = db.Column(db.String(100))

    descricao = db.Column(db.String(200))

    livros = db.relationship('Livro', backref='sessao',
                                lazy='dynamic')
    def __init__(self, localizacao, descricao):
        self.localizacao = localizacao
        self.descricao = descricao        
    def __repr__(self):
        return '{} ({})'.format(self.localizacao, self.descricao)
        
