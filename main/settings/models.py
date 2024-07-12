from main import db

class Setting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(120), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
