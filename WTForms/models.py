from flask_sqlalchemy import SQLAlchemy 

GENERIC_IMAGE = "https://images.unsplash.com/photo-1519590125943-c41c30ed6477?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2976&q=80"

db = SQLAlchemy()

class Pet(db.Model):

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        return self.photo_url or GENERIC_IMAGE

def connect_db(app):
    db.app = app
    db.init_app(app)
    db.create_all()