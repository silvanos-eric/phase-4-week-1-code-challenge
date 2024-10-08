from flask import Flask
from flask_migrate import Migrate
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db.init_app(app)
Migrate(app, db)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
