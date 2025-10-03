from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Booking  # import your Booking model

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    bookings = Booking.query.all()
    return render_template('index.html', bookings=bookings)

@bp.route('/book', methods=['POST'])
def book():
    booking = Booking(
        customer_name=request.form['customer_name'],
        room_number=request.form['room_number'],
        booking_date=request.form['booking_date'],
        time_slot=request.form['time_slot'],
        aadhaar_no=request.form['aadhaar_no'],
        pan_no=request.form['pan_no'],
        email=request.form['email'],
        food_pref=request.form['food_pref']
    )
    db.session.add(booking)
    db.session.commit()
    return redirect(url_for('main.index'))

