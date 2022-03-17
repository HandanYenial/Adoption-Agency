from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, URLField, TextAreaField,BooleanField,SelectField
from wtforms.validators import InputRequired, Optional,URL,NumberRange,Length

class AddNewPetForm(FlaskForm):
    """Form for adding a new pet"""
    name = StringField("Name" , validators=[InputRequired()])
    species  = SelectField("Species", 
                            choices=[("cat","Cat"),("dog","Dog"),("porcupine","Porcupine")])
    photo_url = URLField("Photo URL", validators=[Optional(),URL()])
    age = FloatField("Age(y.m)", validators=[Optional(), NumberRange(min=0, max=30)])
    notes=TextAreaField("Notes" , validators=[Optional(), Length(min=10)])

class EditPetForm(FlaskForm):
    """Form that enables to edit photo url,notes and availablity"""
    photo_url = URLField("Photo URL", validators=[Optional(),URL()])
    notes     = TextAreaField("Notes" , validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")
