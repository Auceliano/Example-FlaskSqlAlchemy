from TechApp import db, models
from TechApp.models import Usuario, Endereco
from management import *
import unittest

class TestCase(unittest.TestCase):
	def setUp(self):
		# create the database
		db.drop_all()
		db.create_all()
	#Testes da entidade Usuário
	def test_obter_usuarios(self):
		db.session.add(Usuario('Auceliano', '88 9 9247 3860', 'n.a.n.d.o_@outlook.com'))
		db.session.add(Usuario('José', '88 9 9999 9999', 'umoutroalguem@outlook.com'))
		db.session.add(Usuario('Um Zé ninguem', '88 8 8888 8888', 'zéninguem@outlook.com'))
		db.session.commit()
		usuarios = obter_usuarios()
		self.assertEqual(len(usuarios),3)
		self.assertEqual(usuarios[0].nome, 'Auceliano')
		self.assertEqual(usuarios[1].nome, 'José')
		self.assertEqual(usuarios[2].nome, 'Um Zé ninguem')

	def test_inserir_usuario(self):
		inserir_usuario('Desmeliedison Jerry Junior', '88 9 6969 9696', 'desmeliedison@gmail.com')
		usuario = Usuario.query.filter_by(nome='Desmeliedison Jerry Junior').first()
		self.assertEqual(usuario.nome, 'Desmeliedison Jerry Junior')
		self.assertEqual(usuario.telefone, '88 9 6969 9696')
		self.assertEqual(usuario.email, 'desmeliedison@gmail.com')

	def test_atualizar_usuario(self):
		inserir_usuario('Desmeliedison Jerry Junior', '88 9 6969 9696', 'desmeliedison@gmail.com')
		atualizar_usuario(0, 'Atualizado', 'Atualizado', 'Atualizado')
		user = Usuario.query.get(0)
		self.assertEqual(user, None)

	def test_deletar_usuario(self):
		inserir_usuario('Desmeliedison Jerry Junior', '88 9 6969 9696', 'desmeliedison@gmail.com')
		deletar_usuario(0)
		user = Usuario.query.get(0)
		self.assertEqual(user, None)
	#Fim testes entidade Usuário


if __name__ == '__main__':
	unittest.main()