from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from TechApp import db

###
class Usuario(db.Model):
    """Entidade Usuário"""
    id = db.Column(
        db.Integer,
        primary_key = True)

    nome = db.Column(db.String(100))

    telefone = db.Column(db.String(20))

    email = db.Column(db.String(50))

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
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
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
        self.descricao = descricao
        self.localizacao = localizacao
        




              


        


###
class Funcionario(db.Model):
    id = db.Column(
        db.Integer,
        primary_key = True)

    id_loja = db.Column(
        db.Integer,
        db.ForeignKey('loja.id'))

class Loja(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True)
    titulo = db.Column(db.String(20))        
    funcs = db.relationship(
        'Funcionario',
        backref='loja',
        lazy='dynamic')
    def __init__(self, t):
        self.titulo = t

class Pessoa(db.Model):
    id = db.Column(
            db.Integer,
            primary_key = True)

    id_telefone = db.Column(
            db.Integer,
            db.ForeignKey('telefone.id'))
    
    telefone = db.relationship(
            'Telefone',
            backref='pessoa',
            uselist=False)

class Telefone(db.Model):
        id = db.Column(
        db.Integer,
        primary_key=True)

matriculas = db.Table(
    
    'matriculas',
    
    db.Column('aluno_id',
            db.Integer,
            db.ForeignKey('aluno.id')),
    
    db.Column('disciplina_id',
            db.Integer,
            db.ForeignKey('disciplina.id')) )

class Aluno(db.Model):
    id = db.Column(
    db.Integer,
    primary_key = True)
    
    disciplinas = db.relationship(
    
        'Disciplina',
    
        secondary=matriculas,
    
        backref=db.backref(
            'aluno',
            lazy='dynamic'))

class Disciplina(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True)
    
    alunos = db.relationship(
        'Aluno',
        secondary=matriculas,
        backref=db.backref(
        'disciplina',
        lazy='dynamic'))




#obter_lojas = lambda: Loja.querry.all()
def obter_lojas():
    return Loja.query.all()

def inserir_loja(titulo):
    loja = Loja(titulo)
    db.session.add(loja)
    db.session.commit()

def atualizar_loja(id, titulo):
    loja = Loja.query.get(id)
    
    if loja is not None:
        loja.titulo = titulo
        db.session.commit()
    else:
        raise Exception ("Loja nao existe!")

def remover_loja(id):
    loja = Loja.query.get(id)
    
    if loja is not None:
        db.session.delete(loja)
        db.session.commit()
        return True
    else:
        return False
        