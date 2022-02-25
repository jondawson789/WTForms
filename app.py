from models import db, connect_db, Pet
from flask import Flask, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "oh-so-secret"

toolbar = DebugToolbarExtension(app)
connect_db(app)
db.create_all()

DEFAULT_URL = "https://as1.ftcdn.net/v2/jpg/03/53/11/00/1000_F_353110097_nbpmfn9iHlxef4EDIhXB1tdTD0lcWhG9.jpg"

@app.route('/')
def show_pets():
    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(name = form.name.data, species = form.species.data, photo_url = form.photo_url.data, age = form.age.data, notes = form.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("pet-add-form.html", form=form)

@app.route('/pet/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template("pet-edit-form.html", form=form, pet=pet)