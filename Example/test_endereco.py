from TechApp import db, models
from TechApp.models import Usuario, Endereco
from management import *
import unittest

class TestCase(unittest.TestCase):
	def setUp(self):
		# create the database
		db.drop_all()
		db.create_all()
	
	#Testes da entidade Endereço
	def test_inserir_endereco(self):
		endereco = inserir_endereco('62823-000', 'Jaguaruana', 'Sitio Saquinho s/n')
		self.assertEqual(endereco.cep, '62823-000')

	def test_atualizar_endereco(self):
		endereco = inserir_endereco('62823-000', 'Jaguaruana', 'Sitio Saquinho s/n')
		atualizar_endereco(endereco.id, 'Atualizado', 'Atualizado', 'Atualizado')
		self.assertEqual(endereco.cep, 'Atualizado')

	def test_deletar_endereco(self):
		endereco = inserir_endereco('62823-000', 'Jaguaruana', 'Sitio Saquinho s/n')
		adress = deletar_endereco(endereco.id)
		self.assertEqual(adress, True)

	def test_obter_endereco(self):
		endereco = inserir_endereco('62823-000', 'Jaguaruana', 'Sitio Saquinho s/n')
		endereco1 = inserir_endereco('62800-000', 'Aracati', 'Cajueiro')
		endereco2 = inserir_endereco('62823-222', 'Jaguaretama', 'Sitio s/n')
		endereco3 = obter_endereco(endereco2.id)
		self.assertEqual(endereco2, endereco3)
	#Fim testes entidade Usuário

if __name__ == '__main__':
	unittest.main()