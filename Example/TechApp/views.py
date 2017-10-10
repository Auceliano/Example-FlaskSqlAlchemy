from TechApp import app
from flask import render_template, redirect, url_for, request, session, flash
from management import inserir_usuario, inserir_endereco, vincular_user_adress,\
obter_usuarios, deletar_usuario, validar_login
 


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
def cadastrarusuario():
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
		return render_template('cadastrarusuario.html', usuario = session['usuario'], lista_usuarios = obter_usuarios(), Alterar = 'alterarUsuario', Excluir = 'excluirUsuario')
	return redirect(url_for('homepage'))

@app.route('/cadastrarusuario/excluir/<int:index>')
def excluirUsuario(index):
	if 'usuario' in session and session['usuario']['Tipo'] == 'A':
		user = deletar_usuario(index)
		#deletar_endereco(user.endereco.id)
		flash('Usuário removido com sucesso!')
		return redirect(url_for('cadastrarusuario'))
	return redirect(url_for('homepage'))

@app.route('/cadastrarlivro')
def cadastrarlivro():
	if 'usuario' in session:
		return render_template('cadastrarlivro.html', usuario = session['usuario'])
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
