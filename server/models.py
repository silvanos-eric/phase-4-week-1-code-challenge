from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()


class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'heroes_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    serialize_rules = '-hero', '-power'


class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String, unique=True)

    hero_power_list = db.relationship('HeroPower', backref='hero')
    powers = association_proxy('hero_power_list', 'power')

    serialize_rules = '-hero_power_list.hero',


class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String)

    hero_power_list = db.relationship('HeroPower', backref='power')
    heroes = association_proxy('hero_power_list', 'hero')

    serialize_rules = '-hero_power_list.power',
