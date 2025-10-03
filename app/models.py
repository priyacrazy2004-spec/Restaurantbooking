from . import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    room_number = db.Column(db.Integer, nullable=False)
    booking_date = db.Column(db.String(20), nullable=False)
    time_slot = db.Column(db.String(50), nullable=False)
    aadhaar_no = db.Column(db.String(20), nullable=False)
    pan_no = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    food_pref = db.Column(db.String(20), nullable=False)
