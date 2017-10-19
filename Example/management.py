from TechApp import db, models
from TechApp.models import Usuario, Endereco, Emprestimo, Livro, Sessao
from datetime import date


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
	
def vincular_emprestimo_livro(emprestimo_id, livro_id):
	emprestimo = Emprestimo.query.get(emprestimo_id)
	livro = Livro.query.get(livro_id)
	if emprestimo and livro is not None:
		emprestimo.livros.append(livro) 
		livro.emprestimos.append(emprestimo)
		db.session.commit()
		return emprestimo
	else:
		return None

def vincular_livro_sessao(livro_id, sessao_id):
	livro = Livro.query.get(livro_id)
	sessao = Sessao.query.get(sessao_id)
	if livro and sessao is not None:
		livro.sessao_id = sessao.id
		sessao.livros.append(livro)
		db.session.commit()
		return livro
	else:
		return None

#CRUD ENTIDADE USUÁRIO
def obter_usuarios():
	users = Usuario.query.all()
	
	lista_usuarios = list()

	if users is not None:
		for item in users:
			if item.endereco is not None:
				lista_usuarios.append({'Id':item.id, 'Nome':item.nome, 'Telefone':item.telefone, 'Email':item.email, 'Senha':item.senha, 'Id_Endereço':item.endereco.id, 'Rua':item.endereco.rua, 'Cep':item.endereco.cep, 'Cidade':item.endereco.cidade, 'Tipo':item.tipo,})
			else:
				lista_usuarios.append({'Id':item.id, 'Nome':item.nome, 'Telefone':item.telefone, 'Email':item.email, 'Senha':item.senha, 'Tipo':item.tipo,})	

		return lista_usuarios
	else:
		return None

def obter_usuario(usuario_id):
	user = Usuario.query.get(usuario_id)
	if user is not None:
		return user
	else:
		return None

def validar_login(usuario_email, usuario_senha):
	user = Usuario.query.filter(Usuario.email==usuario_email, Usuario.senha==usuario_senha).first()
	if user is not None:
		return ({'id':user.id, 'Email':user.email, 'Senha':user.senha, 'Nome':user.nome, 'Telefone':user.telefone, 'Tipo':user.tipo})
	else:
		return None


def inserir_usuario(nome, telefone, email, senha, tipo):
	user = Usuario(nome, telefone, email, senha, tipo)
	db.session.add(user)
	db.session.commit()
	return user

def atualizar_usuario(id, nome, telefone, email, senha, tipo):
	user = Usuario.query.get(id)
	if user is not None:
		user.nome = nome
		user.telefone = telefone
		user.email = email
		user.senha = senha
		user.tipo = tipo
		db.session.commit()
	else:
		return None

def deletar_usuario(id):
	user = Usuario.query.get(id)

	if user is not None:
		db.session.delete(user)
		db.session.commit()
		return user
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

def obter_livros():
	livros = Livro.query.all()
	lista_livros = list()
	if livros is not None:
		for item in livros:
			lista_livros.append({'Id':item.id, 'Título':item.titulo, 'Autor':item.autor, 'Sessão_id':item.sessao_id, 'Localização':obter_sessao(item.sessao_id).localizacao, 'Descricão': obter_sessao(item.sessao_id).descricao})
		return lista_livros
	else:
		return None

#CRUD ENTIDADE EMPRESTIMO
def inserir_emprestimo(data_emprestimo, data_devolucao, id_usuario, livro):
	emprestimo = Emprestimo(date(*[int(x) for x in data_emprestimo.split('-')]), date(*[int(x) for x in data_devolucao.split('-')]), id_usuario, obter_livro(livro))
	db.session.add(emprestimo)
	db.session.commit()
	return emprestimo

def atualizar_emprestimo(id, data_emprestimo, data_devolucao, usuario, livro):
	emprestimo = Emprestimo.query.get(id)
	if emprestimo is not None:
		emprestimo.id_usuario = id
		emprestimo.livros.pop()
		emprestimo.livros.append(obter_livro(livro))
		emprestimo.data_emprestimo = date(*[int(x) for x in data_emprestimo.split('-')])
		emprestimo.data_devolucao = date(*[int(x) for x in data_devolucao.split('-')])
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

def obter_emprestimos():
	emprestimos = Emprestimo.query.all()
	lista_emprestimos = list()
	if emprestimos is not None:
		for item in emprestimos:
			lista_emprestimos.append({'Id':item.id, 'Usuário':obter_usuario(item.id_usuario).nome, 'Id_User':item.id_usuario, 'Livros':item.livros[0].titulo, 'Data de Emprestimo':item.data_emprestimo, 'Data de Devolução':item.data_devolucao})
		return lista_emprestimos
	else:
		return None