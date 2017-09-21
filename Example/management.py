from TechApp import db, models
from TechApp.models import *


def vincular_user_adress(user_id, adress_id):
	user = Usuario.query.get(user_id)
	adress = Endereco.query.get(adress_id)
	if user and adress is not None:
		user.endereco = adress
		db.session.commit()	
		return user
	else:
		return None

def vincular_user_emprestimo(user_id, emprestimo_id):
	user = Usuario.query.get(user_id)
	emprestimo = Emprestimo.query.get(emprestimo_id)
	if user and Emprestimo is not None:
		user.emprestimo = emprestimo
		emprestimo.id_usuario = user_id
		db.session.commit()	
		return user
	else:
		return None
	

#CRUD ENTIDADE USUÁRIO
def obter_usuarios():
	return Usuario.query.all()

def inserir_usuario(nome, telefone, email):
	user = Usuario(nome, telefone, email)
	db.session.add(user)
	db.session.commit()
	return user

def atualizar_usuario(id, nome, telefone, email):
	user = Usuario.query.get(id)
	if user is not None:
		user.nome = nome
		user.telefone = telefone
		user.email = email
		db.session.commit()
	else:
		return None

def deletar_usuario(id):
	user = Usuario.query.get(id)

	if user is not None:
		db.session.delete(user)
		db.session.commit()
		return True
	else:
		return None

#CRUD ENTIDADE ENDEREÇO
def inserir_endereco(cep, cidade, rua):
	adress = Endereco(cep, cidade, rua)
	db.session.add(adress)
	db.session.commit()
	return adress

def atualizar_endereco(id, cep, cidade, rua):
	adress = Endereco.query.get(id)
	
	if adress is not None:
		adress.cep = cep
		adress.cidade = cidade
		adress.rua = rua
		db.session.commit()
		return adress
	else:
		return None

def deletar_endereco(id):
	adress = Endereco.query.get(id)

	if adress is not None:
		db.session.delete(adress)
		db.session.commit()
		return True
	else:
		return None

def obter_endereco(id):
	adress = Endereco.query.get(id)

	if adress is not None:
		return adress
	else:
		return None

#CRUD ENTIDADE SESSAO
def inserir_sessao(localizacao, descricao):
	sessao = Sessao(localizacao, descricao)
	db.session.add(sessao)
	db.session.commit()
	return sessao

def atualizar_sessao(id, localizacao, descricao):
	sessao = Sessao.query.get(id)
	if sessao is not None:
		sessao.localizacao = localizacao
		sessao.descricao = descricao
		db.session.commit()
		return sessao
	else:
		return None

def deletar_sessao(id):
	sessao = Sessao.query.get(id)
	if sessao is not None:
		db.session.delete(sessao)
		db.session.commit()
		return sessao
	else:
		return None

def obter_sessao(id):
	sessao = Sessao.query.get(id)
	if sessao is not None:
		return sessao
	else:
		return None


#CRUD ENTIDADE LIVRO
def inserir_livro(titulo, autor):
	livro = Livro(titulo, autor)
	db.session.add(livro)
	db.session.commit()
	return livro

def atualizar_livro(id, titulo, autor):
	livro = Livro.query.get(id)
	if livro is not None:
		livro.titulo = titulo
		livro.autor = autor
		db.session.commit()
		return livro
	else:
		return None

def deletar_livro(id):
	livro = Livro.query.get(id)
	if livro is not None:
		db.session.delete(livro)
		db.session.commit()
		return livro
	else:
		return None

def obter_livro(id):
	livro = Livro.query.get(id)
	if livro is not None:
		return livro
	else:
		return None

#CRUD ENTIDADE EMPRESTIMO
def inserir_emprestimo(data_emprestimo, data_devolucao):
	emprestimo = Emprestimo(data_emprestimo, data_devolucao)
	db.session.add(emprestimo)
	db.session.commit()
	return emprestimo

def atualizar_emprestimo(id, data_emprestimo, data_devolucao):
	emprestimo = Emprestimo.query.get(id)
	if emprestimo is not None:
		emprestimo.data_emprestimo = data_emprestimo
		emprestimo.data_devolucao = data_devolucao
		db.session.commit()
		return emprestimo
	else:
		return None

def deletar_emprestimo(id):
	emprestimo = Emprestimo.query.get(id)
	if emprestimo is not None:
		db.session.delete(emprestimo)
		db.session.commit()
		return emprestimo
	else:
		return None

def obter_emprestimo(id):
	emprestimo = Emprestimo.query.get(id)
	if emprestimo is not None:
		return emprestimo
	else:
		return None