from TechApp import db, models
from TechApp.models import Usuario, Endereco
from management import *
import unittest

class TestCase(unittest.TestCase):
	def setUp(self):
		# create the database
		db.drop_all()
		db.create_all()

	#Testes da Entidade Emprestimo
	def test_inserir_emprestimo(self):
		emprestimo = inserir_emprestimo(datetime.date(datetime.now()), datetime.date(datetime.now().replace(2018, 9, 19, 0, 0, 0, 0)))
		emprestimo2 = Emprestimo.query.get(emprestimo.id)
		self.assertEqual(emprestimo.data_emprestimo, emprestimo2.data_emprestimo)

	def test_atualizar_emprestimo(self):
		emprestimo = inserir_emprestimo(datetime.date(datetime.now()), datetime.date(datetime.now().replace(2019, 9, 20, 0, 0, 0, 0)))
		emprestimo2 = atualizar_emprestimo(emprestimo.id, emprestimo.data_emprestimo, datetime.date(datetime.now().replace(2050, 9, 20 ,0 ,0 ,0 ,0)))
		self.assertEqual(emprestimo2.data_devolucao, datetime.now().replace(2050, 9, 20, 0, 0, 0, 0))

	def test_deletar_emprestimo(self):
		emprestimo = inserir_emprestimo(datetime.date(datetime.now()), datetime.date(datetime.now().replace(2019, 9, 20, 0, 0, 0, 0)))
		emprestimo2 = deletar_emprestimo(emprestimo.id)
		emprestimo3 = Emprestimo.query.get(emprestimo.id)
		self.assertEqual(emprestimo3, None)

	def test_obter_emprestimo(self):
		emprestimo = inserir_emprestimo(datetime.date(datetime.now()), datetime.date(datetime.now().replace(2019, 9, 20, 0, 0, 0, 0)))
		emprestimo1 = inserir_emprestimo(datetime.date(datetime.now()), datetime.date(datetime.now().replace(2020, 9, 20, 0, 0, 0, 0)))
		emprestimo2 = inserir_emprestimo(datetime.date(datetime.now()), datetime.date(datetime.now().replace(2021, 9, 20, 0, 0, 0, 0)))
		emprestimo3 = obter_emprestimo(emprestimo2.id)
		self.assertEqual(emprestimo2.data_devolucao, emprestimo3.data_devolucao)		

if __name__ == '__main__':
	unittest.main()