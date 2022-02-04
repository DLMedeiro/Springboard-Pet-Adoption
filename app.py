from flask import Flask, request, render_template, redirect, flash, session
from flask.templating import render_template_string

from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.util.langhelpers import method_is_overridden
from models import db, connect_db, Pet
from flask_sqlalchemy import SQLAlchemy
from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "Pet_Adoption"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route("/")
def home():
    """Landing page"""

    list_of_pets = Pet.query.all()

    return render_template("index.html", list_of_pets = list_of_pets)

@app.route('/addpet', methods = ['GET', 'POST'])

def add_pet():
    """Add pet, and posts to database.  Page will redirect to form if fields are not completed"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes)
        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('add_pet.html', form = form)

@app.route('/<int:pet_id>/details')
def pet_detail(pet_id):
    pet = Pet.query.get_or_404(pet_id)

    return render_template("pet_detail.html", pet = pet)

@app.route('/<int:pet_id>/editpet', methods = ['GET', 'POST'])
def edit_pet(pet_id):
    """Edit pet details, and posts to database.  Page will redirect to form if fields are not completed"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj = pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()

        return redirect('/' + str(pet_id) + '/details')
    else:
        return render_template('edit_pet.html', form = form, pet = pet)