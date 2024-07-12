from main import db


class Deposit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False, default=0.0)
    type_ = db.Column(db.String(120), nullable=False)