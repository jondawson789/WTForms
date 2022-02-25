from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, NumberRange

class AddPetForm(FlaskForm):
    
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("c","cat"), ("d", "dog"), ("p","porcupine")], validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age",validators=[Optional(), NumberRange(min = 0,max = 30)])
    notes = TextAreaField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
  
    photo_url = StringField("Photo URL",validators=[Optional(), URL()])

    notes = TextAreaField("notes",validators=[Optional()])

    available = BooleanField("Available?")