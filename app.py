from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,connect_db,Pet
from forms import AddNewPetForm,EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "keyforthepets12345"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def pet_list():
    """Shows the list of pets"""
    pets = Pet.query.all()
    return render_template("pet_list.html" , pets=pets)

@app.route('/add' , methods=["GET" , "POST"])
def add_new_pet():
    """Add a new pet"""
    form = AddNewPetForm()

    if form.validate_on_submit():
        name=form.name.data 
        species=form.species.data
        photo_url=form.photo_url.data
        age=form.age.data
        notes=form.notes.data
        pet = Pet(name=name, species=species, photo_url=photo_url,age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"{name} is added")
        return redirect("/")

    else:
        return render_template("add_pet.html" , form=form)

@app.route("/<int:pet_id>" , methods=["GET" , "POST"])
def edit_pets(pet_id):
    """Display and edit pets"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.photo_url = form.photo_url.data
        pet.available = form.available.data
               
        db.session.commit()
        flash(f"{pet.name} is updated")

        return redirect("/")

    else:
        return render_template("pet_edit.html" , form=form , pet=pet)
