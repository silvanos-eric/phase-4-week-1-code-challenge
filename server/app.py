from flask import Flask
from flask_migrate import Migrate
from models import db, Hero, HeroPower, Power

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db.init_app(app)
Migrate(app, db)


@app.route('/')
def get_index():
    """Return a string indicating that the API is live."""
    return 'Superheroes API'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
