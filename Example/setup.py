from TechApp import db
from management import vincular_user_adress, inserir_usuario, inserir_endereco

db.drop_all() 
db.create_all() 

vincular_user_adress(\
	inserir_usuario('Auceliano', '88 9 9247 3860', 'admin', 'admin', 'A').id,\
	inserir_endereco('62823-000', 'Jaguaruana', 'Sitio Saquinho s/n').id)

print('done.')