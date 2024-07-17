from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from .models import User 
from main import db, login_manager  
import requests

auth_bp = Blueprint('auth_bp', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth_bp.route('/signup', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        data = request.form
        recaptcha_response = request.form['g-recaptcha-response']
        secret = '6LepKQsqAAAAANXeGSPJcyBfxg5yfCb74ndotxJX'
        recaptcha_data = {
            'secret': secret,
            'response': recaptcha_response
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=recaptcha_data)
        result = response.json()

        if not result.get('success'):
            flash('reCAPTCHA verification failed. Please try again.', 'danger')
            return redirect(url_for('auth_bp.create_user'))

        new_user = User(
            username=data['username'],
            email=data['email'],
            password=generate_password_hash(data['password'], method='pbkdf2:sha256'),
            country=data['country'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            home_address=data['home_address'],
            contact=data['contact'],
            balance=0.0
        )

        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('auth_bp.login_page'))

    return render_template('others/signup.html')


@auth_bp.route('/signin', methods=['GET', 'POST'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.dashboard'))
    if request.method == 'POST':
        data = request.form
        print(data)
        user = User.query.filter_by(email=data['email']).first()
        if user and check_password_hash(user.password, data['password']):
            login_user(user, remember=True)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('others/signin.html')


 
@auth_bp.route('/signout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!', 'info')
    return redirect(url_for('auth_bp.login_page'))
