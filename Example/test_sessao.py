from TechApp import db, models
from TechApp.models import Usuario, Endereco
from management import *
import unittest

class TestCase(unittest.TestCase):
	def setUp(self):
		# create the database
		db.drop_all()
		db.create_all()

	#Testes da Entidade Sessao
	def test_inserir_sessao(self):
		sessao = inserir_sessao('Prateleira 1', 'artigos academicos')
		self.assertEqual(sessao.descricao, 'artigos academicos')

	def test_atualizar_sessao(self):
		sessao = inserir_sessao('Prateleira 1', 'artigos academicos')
		atualizar_sessao(sessao.id, 'Atualizado', 'Atualizado')
		self.assertEqual(sessao.descricao, 'Atualizado' )

	def test_deletar_sessao(self):
		sessao = inserir_sessao('Prateleira 1', 'artigos academicos')
		sessao2 = deletar_sessao(sessao.id)
		self.assertEqual(sessao, sessao2)

	def test_obter_sessao(self):
		sessao = inserir_sessao('Prateleira 1', 'artigos academicos')
		sessao2 = obter_sessao(sessao.id)
		self.assertEqual(sessao, sessao2)
	#Fim testes entidade Sessao

if __name__ == '__main__':
	unittest.main()