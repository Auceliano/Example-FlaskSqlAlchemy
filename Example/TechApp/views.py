from TechApp import app
from flask import render_template, redirect, url_for, request, session, flash
from management import inserir_usuario, inserir_endereco, vincular_user_adress,\
obter_usuarios, obter_usuario, atualizar_usuario, atualizar_endereco,\
deletar_usuario, validar_login, obter_livros, obter_livro, inserir_livro,\
inserir_sessao, vincular_livro_sessao, deletar_livro, deletar_sessao, obter_sessao,\
atualizar_livro, atualizar_sessao
 


@app.route('/') 
@app.route('/home')
def homepage():
	if 'usuario' in session:
		return render_template('index.html', usuario = session['usuario'])
	return render_template('index.html', usuario = None)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if 'usuario' in session:
		return redirect(url_for('homepage'))
	if request.method == 'POST':
		email = request.form['email']
		senha = request.form['senha']
		if validar_login(email, senha):
			session['usuario'] = validar_login(email, senha)
			return redirect(url_for('homepage'))

	return render_template('login.html')


@app.route('/logout')
def logout():
	session.pop('usuario', None)
	return redirect(url_for('homepage'))


@app.route('/cadastrarusuario', methods=['GET', 'POST'])
def cadastrarUsuario():
	if 'usuario' in session and session['usuario']['Tipo'] == 'A':
		if request.method == 'POST':
			nome = request.form['nome']
			telefone = request.form['telefone']
			email = request.form['email']
			senha = request.form['senha']
			rua = request.form['rua']
			cep = request.form['cep']
			cidade = request.form['cidade']
			tipo = request.form['tipo']
			user = inserir_usuario(nome, telefone, email, senha, tipo)
			endereco = inserir_endereco(cep, cidade, rua)
			vincular_user_adress(user.id, endereco.id)
			flash('Usuário cadastrado com sucesso!')
		return render_template('cadastrarusuario.html', usuario = session['usuario'], lista = obter_usuarios(), Alterar = 'alterarUsuario', Excluir = 'excluirUsuario')
	return redirect(url_for('homepage'))

@app.route('/cadastrarusuario/excluir/<int:index>')
def excluirUsuario(index):
	if 'usuario' in session and session['usuario']['Tipo'] == 'A':
		user = deletar_usuario(index)
		#deletar_endereco(user.endereco.id)
		flash('Usuário removido com sucesso!')
		return redirect(url_for('cadastrarUsuario'))
	return redirect(url_for('homepage'))

@app.route('/cadastrarusuario/alterar/<int:index>', methods=['GET', 'POST'])
def alterarUsuario(index):
	if 'usuario' in session and session['usuario']['Tipo'] == 'A':
		if request.method == 'POST':
			nome = request.form['nome']
			telefone = request.form['telefone']
			email = request.form['email']
			senha = request.form['senha']
			rua = request.form['rua']
			cep = request.form['cep']
			cidade = request.form['cidade']
			tipo = request.form['tipo']
			atualizar_usuario(index, nome, telefone, email, senha, tipo)
			atualizar_endereco(index, cep, cidade, rua)
			flash('Usuário atualizado com sucesso!')
			return redirect(url_for('cadastrarUsuario'))
		return render_template('cadastrarusuario.html', usuario = session['usuario'], lista = obter_usuarios(), Update = obter_usuario(index), index = index, Alterar = 'alterarUsuario', Excluir = 'excluirUsuario')
	return redirect(url_for('homepage'))

@app.route('/cadastrarlivro/alterar/<int:index>', methods=['GET', 'POST'])
def alterarLivro(index):
	if 'usuario' in session and session['usuario']['Tipo'] == 'A':
		if request.method == 'POST':
			titulo = request.form['titulo']
			autor = request.form['autor']
			localizacao = request.form['localizacao']
			descricao = request.form['descricao']
			atualizar_livro(index, titulo, autor)
			atualizar_sessao(index, localizacao, descricao)
			flash('Livro atualizado com sucesso!')
			return redirect(url_for('cadastrarLivro'))
		return render_template('cadastrarlivro.html', usuario = session['usuario'], lista = obter_livros(), Update = obter_sessao(index), index = index, Alterar = 'alterarLivro', Excluir = 'excluirLivro')
	return redirect(url_for('homepage'))

@app.route('/cadastrarlivro/excluir/<int:index>')
def excluirLivro(index):
	if 'usuario' in session and session['usuario']['Tipo'] == 'A':
		livro = deletar_livro(index)
		sessao = deletar_sessao(index)
		#deletar_endereco(user.endereco.id)
		flash('Livro removido com sucesso!')
		return redirect(url_for('cadastrarLivro'))
	return redirect(url_for('homepage'))


@app.route('/cadastrarlivro', methods=['GET', 'POST'])
def cadastrarLivro():
	if 'usuario' in session and session['usuario']['Tipo'] == 'A':
		if request.method == 'POST':
			titulo = request.form['titulo']
			autor = request.form['autor']
			localizacao = request.form['localizacao']
			descricao = request.form['descricao']
			livro = inserir_livro(titulo, autor)
			sessao = inserir_sessao(localizacao, descricao)
			vincular_livro_sessao(livro.id,sessao.id)
			flash('Livro cadastrado com sucesso!')
		return render_template('cadastrarlivro.html', usuario = session['usuario'], lista = obter_livros(), Alterar = 'alterarLivro', Excluir = 'excluirLivro')
	return redirect(url_for('homepage'))

@app.route('/cadastraremprestimo')
def cadastraremprestimo():
	if 'usuario' in session:
		return render_template('cadastraremprestimo.html', usuario = session['usuario'])
	return redirect(url_for('homepage'))

@app.route('/about')
def sobre():
	if 'usuario' in session:
		return render_template('sobre.html', usuario = session['usuario'])
	return render_template('sobre.html', usuario = None)
