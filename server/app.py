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


@app.route('/heroes', methods=['GET'])
def get_heroes():
    """Get a list of all the heroes."""
    heroes = Hero.query.all()
    return [hero.to_dict(rules=('-hero_power_list', )) for hero in heroes]


@app.route('/heroes/<int:hero_id>')
def hero_by_id(hero_id):
    """Return a hero by id."""
    hero = Hero.query.get(hero_id)

    return hero.to_dict()


if __name__ == '__main__':
    app.run(port=5555, debug=True)
