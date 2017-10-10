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
	def test_vincular_livro_sessao(self):
		user = inserir_usuario('Desmeliedison Jerry Junior', '88 9 6969 9696', 'desmeliedison@gmail.com','admin', 'A')
		
		emprestimo = inserir_emprestimo(datetime.date(datetime.now()), datetime.date(datetime.now().replace(2019, 9, 20, 0, 0, 0, 0)))
		emprestimo1 = inserir_emprestimo(datetime.date(datetime.now()), datetime.date(datetime.now().replace(2020, 9, 20, 0, 0, 0, 0)))
		emprestimo2 = inserir_emprestimo(datetime.date(datetime.now()), datetime.date(datetime.now().replace(2021, 9, 20, 0, 0, 0, 0)))
		
		user_emprestimo = vincular_user_emprestimo(user.id, emprestimo2.id)

		livro = inserir_livro('Java', 'Deitel')
		livro1 = inserir_livro('Como Programar', 'Deitel')
		livro2 = inserir_livro('Java - Como Programar - 8ª Ed. 2010', 'Deitel')

		emprestimo_livro = vincular_emprestimo_livro(emprestimo2.id, livro2.id)

		sessao = inserir_sessao('Estante 2', 'Bloco 1')

		livro_sessao = vincular_livro_sessao(livro2.id, sessao.id)

		self.assertEqual(user_emprestimo.emprestimo.id, emprestimo2.id)
		self.assertEqual(user_emprestimo.id, emprestimo2.id_usuario)
		self.assertEqual(emprestimo_livro.livros[0].id, livro2.id)
		self.assertEqual(Livro.query.get(livro2.id).emprestimos[0].id, emprestimo_livro.id)
		self.assertEqual(livro_sessao.sessao_id, sessao.id)

if __name__ == '__main__':
	unittest.main()