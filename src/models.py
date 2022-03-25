from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()        





class Favoritcharacter(db.Model):
    __tablename__ = 'favoritcharacter'
    id = db.Column(db.Integer, primary_key=True)
    characters_id = db.Column(db.Integer, ForeignKey('character.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    favorit_character = db.relationship('User')
    favorit_character2 = db.relationship('Character')
    
    

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "characters_id": self.characters_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()    

class Favoritplanet(db.Model):
    __tablename__ = 'favoritplanet'
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, ForeignKey('planet.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    pl = db.relationship('User')
    pl1 = db.relationship('Planet')
    
    

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()    

class Favoritspecie(db.Model):
    __tablename__ = 'favoritspecie'
    id = db.Column(db.Integer, primary_key=True)
    specie_id = db.Column(db.Integer, ForeignKey('specie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    sp = db.relationship('User')
    sp1 = db.relationship('Specie')
    

    

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "specie_id": self.specie_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()    

class Favoritstarship(db.Model):
    __tablename__ = 'favoritstarship'
    id = db.Column(db.Integer, primary_key=True)
    starship_id = db.Column(db.Integer, ForeignKey('starship.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    st = db.relationship('User')
    st = db.relationship('Starship')
    

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "starship_id": self.starship_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()    

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    lastname = db.Column(db.String(250), nullable=False)
    homeworld = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    specie = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "homeworld": self.homeworld,
            "gender": self.gender,
            "specie": self.specie
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()    

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()    

class Specie(db.Model):
    __tablename__ = 'specie'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    homeworld = db.Column(db.String(250), nullable=False)
    lenguage = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "homeworld": self.homeworld,
            "lenguage": self.lenguage
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()    

class Starship(db.Model):
    __tablename__ = 'starship'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer
        } 

    def save(self):
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()             