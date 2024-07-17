from main import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    profile_picture = db.Column(db.String(200), nullable=True)
    home_address = db.Column(db.String(200), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    job_title = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    balance = db.Column(db.Float, nullable=False, default=0.0)
    account_type = db.Column(db.String(200), )
    driver_license = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'
