from flask import Flask, request
from flask_migrate import Migrate
from models import db, Hero, HeroPower, Power

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db.init_app(app)
Migrate(app, db)


@app.route('/')
def index():
    """Return a string indicating that the API is live."""

    return '''
        <h1>Superheroes API</h1>
    
        <h2><code>GET /</code></h2>
        <p>Returns a welcome message indicating the API is live <em>(This page)</em>.</p>
    
        <h2><code>GET /heroes</code></h2>
        <p>Returns a list of all heroes, excluding their related powers.</p>
    
        <h2><code>GET /heroes/&lt;id&gt;</code></h2>
        <p>Fetches details for a specific hero by their ID. Returns 404 Not Found if the hero is not found.</p>
    
        <h2><code>GET /powers</code></h2>
        <p>Returns a list of all available powers.</p>
    
        <h2><code>GET /powers/&lt;id&gt;</code></h2>
        <p>Returns details of a specific power by ID. Returns 404 Not Found if the power is not found.</p>
    
        <h2><code>PATCH /powers/&lt;id&gt;</code></h2>
        <p>Allows updates to a power's details using a JSON payload. Returns 404 Not Found if the power is not found.</p>
    
        <h2><code>POST /hero_powers</code></h2>
        <p>Creates a new hero-power relationship, with custom strength, using a JSON payload. Returns 400 Bad Request if the JSON payload is invalid.</p>
    '''


@app.route('/heroes', methods=['GET'])
def get_heroes():
    """Get a list of all the heroes."""

    heroes = Hero.query.all()

    return [hero.to_dict(rules=('-hero_powers', )) for hero in heroes]


@app.route('/heroes/<int:id>')
def hero_by_id(id):
    """Return a hero by id."""

    hero = Hero.query.get(id)

    if not hero:
        return {'error': 'Hero not found'}, 404

    return hero.to_dict()


@app.route('/powers')
def powers():
    """Get a list of all the powers."""

    powers = Power.query.all()
    return [power.to_dict(rules=('-hero_powers', )) for power in powers]


@app.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def get_or_update_power(id):
    """Get a power by id or update a power by id."""

    power = Power.query.get(id)

    if not power:
        return {'error': 'Power not found'}

    if request.method == 'GET':
        if not power:
            return {'error': 'Power not found'}, 404

        return power.to_dict(rules=('-hero_powers', ))

    elif request.method == 'PATCH':
        try:
            for key, value in request.json.items():
                setattr(power, key, value)
            db.session.commit()
        except ValueError as e:
            return {'error': str(e)}, 400
        except:
            return {'error': ['Validation errors']}, 400

        return power.to_dict(rules=('-hero_powers', ))


@app.route('/hero_powers', methods=['POST'])
def hero_powers():
    """Create a new hero power."""

    data = request.json
    try:
        new_hero_power = HeroPower(strength=data.get('strength'),
                                   power_id=data.get('power_id'),
                                   hero_id=data.get('hero_id'))
        db.session.add(new_hero_power)
        db.session.commit()

        return new_hero_power.to_dict(), 201
    except ValueError as e:
        return {'errors': str(e)}, 400
    except:
        return {'error': ['Validation errors']}, 400


if __name__ == '__main__':
    app.run(port=5555, debug=True)
