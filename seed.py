"""Seed file to make sample data for pet_adoption db."""

from os import stat_result
from typing import ByteString
from models import Pet, db
from app import app

# (venv) python seed.py

#Create tables
db.drop_all()
db.create_all()

#If table isn't empty, empty it
Pet.query.delete()

#Create Pets
maggie = Pet(name = "Maggie", species = "Dog", photo_url = "https://images.pexels.com/photos/825947/pexels-photo-825947.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", age = "5", notes = "Loves belly rubs", available = False)
finn = Pet(name = "Finn", species = "Dog", photo_url = "https://images.pexels.com/photos/2853422/pexels-photo-2853422.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", age = "5", notes = "Afraid of fireworks", available = False)
kevin = Pet(name = "Kevin", species = "cat", photo_url = "https://images.pexels.com/photos/1741205/pexels-photo-1741205.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", age = "2", notes = "Easily distracted", available = True)
mo = Pet(name = "Mo", species = "Cat", photo_url = "https://images.pexels.com/photos/2558605/pexels-photo-2558605.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", age = "1", notes = "Perfect nap buddy", available = True)
stu = Pet(name = "Stu", species = "Dog", photo_url = "https://images.pexels.com/photos/1851164/pexels-photo-1851164.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", age = "9", notes = "Loves belly rubs", available = True)

# Add new pet objects to the session
db.session.add(maggie)
db.session.add(finn)
db.session.add(kevin)
db.session.add(mo)
db.session.add(stu)

# Commit 
db.session.commit()