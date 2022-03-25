"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Favoritcharacter, Favoritplanet, Favoritspecie, Favoritstarship, Character, Starship, Planet, Specie


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dev_4geeks.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


db.init_app(app)
Migrate(app, db)

@app.route('/users', methods=['GET'])
def all_user():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    return jsonify(users), 200
    

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    users = User.query.get(id)
    return jsonify(users.serialize()), 200

@app.route('/users', methods=['POST']) 
def create_user():
    name = request.json.get('name')
    email = request.json.get('email')

    user = User()
    user.name = name
    user.email = email

    db.session.add(user)
    db.session.commit()
    
    return jsonify(user.serialize()), 201

@app.route('/users/<int:id>', methods=['PUT']) 
def modificar_user(id):
    name = request.json.get('name')
    email = request.json.get('email')

    user = User.query.get(id)
    user.name = name
    user.email = email

    
    db.session.commit()
    
    return jsonify(user.serialize()), 201

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_users(id):
    users = User.query.get(id)
    db.session.delete(users)
    db.session.commit()

    return jsonify({}), 200   

@app.route('/character', methods=['GET'])
def get_character():
    characters = Character.query.all()
    characters = list(map(lambda character: character.serialize(), characters))
    return jsonify(characters), 200

@app.route('/character/<int:id>', methods=['GET'])
def get_character_by_id(id):
    character = Character.query.get(id)
    return jsonify(character.serialize()), 200

@app.route('/character', methods=['POST'])
def create_character():
    name = request.json.get('name')
    lastname = request.json.get('lastname')
    homeworld = request.json.get('homeworld')
    gender = request.json.get('gender')
    specie = request.json.get('specie')  

    character = Character()
    character.name = name
    character.lastname = lastname
    character.homeworld = homeworld
    character.gender = gender
    character.specie = specie

    db.session.add(character)
    db.session.commit()

    return jsonify(character.serialize()), 201

@app.route('/character/<int:id>', methods=['PUT'])
def update_character(id):
     name = request.json.get('name')
     lastname = request.json.get('lastname')
     homeworld = request.json.get('homeworld')
     gender = request.json.get('gender')
     specie = request.json.get('specie')

     character = Character.query.get(id)
     character.name = name
     character.lastname = lastname
     character.homeworld = homeworld
     character.gender = gender
     character.specie = specie

     db.session.commit()

     return jsonify(character.serialize()), 200

@app.route('/character/<int:id>', methods=['DELETE'])
def delete_character(id):
    character = Character.query.get(id)
    db.session.delete(character)
    db.session.commit()

    return jsonify({}), 200
                  


@app.route('/planet', methods=['GET'])
def get_planet():
    planets = Planet.query.all()
    planets = list(map(lambda planet: planet.serialize(), planets))
    return jsonify(planets), 200

@app.route('/planet/<int:id>', methods=['GET'])
def get_planet_by_id(id):
    planet = Planet.query.get(id)
    return jsonify(planet.serialize()), 200

@app.route('/planet', methods=['POST'])
def create_planet():
    name = request.json.get('name')
    climate = request.json.get('climate')
    population = request.json.get('population')
   

    planet = Planet()
    planet.name = name
    planet.climate = climate
    planet.population = population
    

    db.session.add(planet)
    db.session.commit()

    return jsonify(planet.serialize()), 201

@app.route('/planet/<int:id>', methods=['PUT'])
def update_planet(id):
     name = request.json.get('name')
     climate = request.json.get('climate')
     population = request.json.get('population')
     

     planet = Planet.query.get(id)
     planet.name = name
     planet.climate = climate
     planet.population = population
     

     db.session.commit()

     return jsonify(planet.serialize()), 200

@app.route('/planet/<int:id>', methods=['DELETE'])
def delete_planet(id):
    planet = Planet.query.get(id)
    db.session.delete(planet)
    db.session.commit()

    return jsonify({}), 200


@app.route('/specie', methods=['GET'])
def get_specie():
    species = Specie.query.all()
    species = list(map(lambda specie: specie.serialize(), species))
    return jsonify(species), 200

@app.route('/specie/<int:id>', methods=['GET'])
def get_specie_by_id(id):
    specie = Specie.query.get(id)
    return jsonify(specie.serialize()), 200

@app.route('/specie', methods=['POST'])
def create_specie():
    name = request.json.get('name')
    homeworld = request.json.get('homeworld')
    lenguage = request.json.get('lenguage')
     

    specie = Specie()
    specie.name = name
    specie.homeworld = homeworld
    specie.lenguage = lenguage
   

    db.session.add(specie)
    db.session.commit()

    return jsonify(specie.serialize()), 201

@app.route('/specie/<int:id>', methods=['PUT'])
def update_specie(id):
     name = request.json.get('name')
     homeworld = request.json.get('homeworld')
     lenguage = request.json.get('lenguage')
     

     specie = Specie.query.get(id)
     specie.name = name
     specie.homeworld = homeworld
     specie.lenguage = lenguage
    

     db.session.commit()

     return jsonify(specie.serialize()), 200

@app.route('/specie/<int:id>', methods=['DELETE'])
def delete_specie(id):
    specie = Specie.query.get(id)
    db.session.delete(specie)
    db.session.commit()

    return jsonify({}), 200


@app.route('/starship', methods=['GET'])
def get_starship():
    starships = Starship.query.all()
    starships = list(map(lambda starship: starship.serialize(), starships))
    return jsonify(starships), 200

@app.route('/starship/<int:id>', methods=['GET'])
def get_starship_by_id(id):
    starship = Starship.query.get(id)
    return jsonify(starship.serialize()), 200

@app.route('/starship', methods=['POST'])
def create_starship():
    name = request.json.get('name')
    model = request.json.get('model')
    manufacturer = request.json.get('manufacturer')
    

    starship = Starship()
    starship.name = name
    starship.model = model
    starship.manufacturer = manufacturer
    
    db.session.add(starship)
    db.session.commit()

    return jsonify(starship.serialize()), 201

@app.route('/starship/<int:id>', methods=['PUT'])
def update_starship(id):
     name = request.json.get('name')
     model = request.json.get('model')
     manufacturer = request.json.get('manufacturer')
     

     starship = Starship.query.get(id)
     starship.model = model
     starship.manufacturer = manufacturer

     db.session.commit()

     return jsonify(starship.serialize()), 200

@app.route('/starship/<int:id>', methods=['DELETE'])
def delete_starship(id):
    starship = Starship.query.get(id)
    db.session.delete(starship)
    db.session.commit()

    return jsonify({}), 200


@app.route('/favoritcharacter', methods=['GET'])
def get_fav_character():
    fav_characters = Favoritcharacter.query.all()
    fav_characters = list(map(lambda fav_character: fav_character.serialize(), fav_characters))
    return jsonify(fav_characters), 200

@app.route('/favoritcharacter/<int:id>', methods=['GET'])
def get_fav_character_by_id(id):
    fav_character = Favoritcharacter.query.get(id)
    return jsonify(fav_character.serialize()), 200

@app.route('/favoritcharacter/character/<int:id>', methods=['POST'])
def create_fav_character():
    name = request.json.get('name')
    lastname = request.json.get('lastname')
    homeworld = request.json.get ('homeworld')
    gender = request.json.get('gender')
    specie = request.json.get('specie')

    fav_character = Favoritcharacter()
    fav_character.name = name
    fav_character.lastname = lastname
    fav_character.homeworld = homeworld
    fav_character.gender = gender
    fav_character.specie = specie

    db.session.add(fav_character)
    db.session.commit()
    return jsonify(fav_character.serialize()), 201
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3452)
