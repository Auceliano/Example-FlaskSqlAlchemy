from TechApp import db, models
from TechApp.models import Usuario, Endereco
from management import *
import unittest

class TestCase(unittest.TestCase):
	def setUp(self):
		# create the database
		db.drop_all()
		db.create_all()


	def test_vincular_user_adress(self):
		user = inserir_usuario('Desmeliedison Jerry Junior', '88 9 6969 9696', 'desmeliedison@gmail.com')
		endereco = inserir_endereco('62823-000', 'Jaguaruana', 'Sitio Saquinho s/n')
		result = vincular_user_adress(user.id, endereco.id)
		self.assertEqual(result, True)
		


if __name__ == '__main__':
	unittest.main()