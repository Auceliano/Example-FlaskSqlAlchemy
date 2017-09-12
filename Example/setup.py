from TechApp import db, models
from copy import copy

db.drop_all()
db.create_all()
print('done.')