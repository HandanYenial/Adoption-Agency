from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

PET_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSIdlG6ad40BCCoRTTU1E7no-1XUfYPPGhzsFbo0nc_Bq2s5Lrd2wfHoQpcF7nExwgWsM&usqp=CAU"

class Pet(db.Model):
    __tablename__='pets'

    id        = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name      = db.Column(db.Text, nullable=False)
    species   = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True, default = PET_URL)
    age       = db.Column(db.Integer, nullable=True)
    notes     = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)
