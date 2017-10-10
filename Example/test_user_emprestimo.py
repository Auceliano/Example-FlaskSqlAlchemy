from TechApp import db, models
from TechApp.models import Usuario, Endereco
from management import *
import unittest

class TestCase(unittest.TestCase):
	def setUp(self):
		# create the database
		db.drop_all()
		db.create_all()

	#Testes da Entidade Usuario e Emprestimo
	def test_vincular_user_emprestimo(self):
		user = inserir_usuario('Desmeliedison Jerry Junior', '88 9 6969 9696', 'desmeliedison@gmail.com','admin', 'A')
		emprestimo = inserir_emprestimo(datetime.date(datetime.now()), datetime.date(datetime.now().replace(2019, 9, 20, 0, 0, 0, 0)))
		emprestimo1 = inserir_emprestimo(datetime.date(datetime.now()), datetime.date(datetime.now().replace(2020, 9, 20, 0, 0, 0, 0)))
		emprestimo2 = inserir_emprestimo(datetime.date(datetime.now()), datetime.date(datetime.now().replace(2021, 9, 20, 0, 0, 0, 0)))
		result = vincular_user_emprestimo(user.id, emprestimo2.id)
		self.assertEqual(result.emprestimo.id, emprestimo2.id)
		emprestimo2 = obter_emprestimo(emprestimo2.id)
		self.assertEqual(result.id, emprestimo2.id_usuario)
		


if __name__ == '__main__':
	unittest.main()