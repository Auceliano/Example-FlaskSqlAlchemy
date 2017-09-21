from TechApp import db, models
from TechApp.models import Usuario, Endereco
from management import *
import unittest

class TestCase(unittest.TestCase):
	def setUp(self):
		# create the database
		db.drop_all()
		db.create_all()

	#Testes da Entidade Livro
	def test_inserir_livro(self):
		livro = inserir_livro('Java - Como Programar - 8ª Ed. 2010', 'Deitel')
		livro2 = Livro.query.get(livro.id)
		self.assertEqual(livro, livro2)

	def test_atualizar_livro(self):
		livro = inserir_livro('Java - Como Programar - 8ª Ed. 2010', 'Deitel')
		livro2 = atualizar_livro(livro.id, 'Java Como Programar 8ª Ed. 2010', 'Deitel')
		self.assertEqual(livro.titulo, 'Java Como Programar 8ª Ed. 2010')

	def test_deletar_livro(self):
		livro = inserir_livro('Java - Como Programar - 8ª Ed. 2010', 'Deitel')
		livro2 = deletar_livro(livro.id)
		livro3 = Livro.query.get(livro.id)
		self.assertEqual(livro3, None)

	def test_obter_livro(self):
		livro = inserir_livro('Java', 'Deitel')
		livro1 = inserir_livro('Como Programar', 'Deitel')
		livro2 = inserir_livro('Java - Como Programar - 8ª Ed. 2010', 'Deitel')
		livro3 = obter_livro(livro2.id)
		self.assertEqual(livro2.titulo, livro3.titulo)		
		


if __name__ == '__main__':
	unittest.main()
	#print('teste')