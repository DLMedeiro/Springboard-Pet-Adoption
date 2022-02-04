from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange



class AddPetForm(FlaskForm):
    """Form for adding a pet"""
    name = StringField("Pet Name", validators = [InputRequired(message = "Pet name can't be blank")])
    species = SelectField("Pet Species", 
        choices = [('dog', 'Dog'), ('cat', 'Cat'), ('ppine', 'Porcupine')])
    photo_url = StringField("Pet Photo", validators = [Optional(), URL()])
    age = IntegerField("Pet Age", validators = [Optional(), NumberRange(min=1, max=30, message="Age must be between 1 and 30")])
    notes = StringField("Pet Notes")

class EditPetForm(FlaskForm):
    """Form for editing a pet"""
    name = StringField("Pet Name", validators = [InputRequired(message = "Pet name can't be blank")])
    species = SelectField("Pet Species", 
        choices = [('dog', 'Dog'), ('cat', 'Cat'), ('ppine', 'Porcupine')])
    photo_url = StringField("Pet Photo", validators = [Optional(), URL()])
    age = IntegerField("Pet Age", validators = [Optional(), NumberRange(min=1, max=30, message="Age must be between 1 and 30")])
    notes = StringField("Pet Notes")
    available = BooleanField("Available")
