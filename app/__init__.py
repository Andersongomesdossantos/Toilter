from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/devel/Documentos/python/toilter/storage.db'
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


from app.controllers import default
#from app.models import default
