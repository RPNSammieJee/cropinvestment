from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
import os
import random
import string
from flask_migrate import Migrate
from main import app
from main.reg_blueprints import reg_blueprints
import requests

reg_blueprints(app)
@app.route("/")
def index_page():
    return render_template("index.html")

# Configure mail server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'aigbornajohnrpnsamuel@gmail.com'  # Update with your email
app.config['MAIL_PASSWORD'] = 'sam05mar'  # Update with your email password

mail = Mail(app)

# Helper function to generate random verification code
def generate_verification_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


@app.route('/dashboard')
# @login_required
def dashboard():
    user = current_user
    return render_template('pages/dashboard.html', user=user)

@app.route('/farmers', methods=['GET', 'POST'])
def farmer_page():
    return render_template("pages/farmers.html")

@app.route('/blog', methods=['GET', 'POST'])
def blog_page():
    return render_template("pages/blog.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    return render_template("contact.html")

@app.route('/FAQ', methods=['GET', 'POST'])
def FAQ_page():
    return render_template("FAQ.html")

@app.route('/grow', methods=['GET', 'POST'])
def grow_page():
    return render_template("grow.html")

@app.route('/porfiolio', methods=['GET', 'POST'])
def porfiolio_page():
    return render_template("porfioloo.html")

@app.route('/Privacy', methods=['GET', 'POST'])
def privacy_page():
    return render_template("privacy1.html")

@app.route('/team', methods=['GET', 'POST'])
def team_page():
    return render_template("team.html")

@app.route('/account', methods=['GET', 'POST'])
def account():
    return render_template("pages/account.html", user={})

@app.route('/admin')
def admin_page():
    user = [{},{},{}]
    return render_template("others/admin.html", users=user)

# @app.route('/Dashboard', methods=['GET', 'POST'])
# def dashboard_page():
#     return render_template("dashboard.html")

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    return render_template("others/deposit.html")

@app.route('/withdrawal', methods=['GET', 'POST'])
def withdrawal():
    return render_template("others/withdrawal.html")

@app.route('/transaction', methods=['GET', 'POST'])
def transaction():
    return render_template("pages/transaction.html")

@app.route('/performance', methods=['GET', 'POST'])
def performance():
    return render_template("pages/performance.html")

@app.route('/setting', methods=['GET', 'POST'])
def setting():
    return render_template("setting.html")

@app.route('/signout', methods=['GET', 'POST'])
def signout():
    return render_template("others/signout.html")

@app.route('/blog1', methods=['GET', 'POST'])
def Blog1_page():
    return render_template("blog2.html")

@app.route('/blog2', methods=['GET', 'POST'])
def Blog2_page():
    return render_template("blog3.html")

@app.route('/blog3', methods=['GET', 'POST'])
def Blog3_page():
    return render_template("blog4.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        recaptcha_response = request.form['g-recaptcha-response']
        secret = '6LepKQsqAAAAANXeGSPJcyBfxg5yfCb74ndotxJX'
        data = {
            'secret': secret,
            'response': recaptcha_response
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = response.json()

        if result['success']:
            # Process the form data here (e.g., save to database)
            username = request.form['username']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            confirm_email = request.form['confirm-email']
            home_address = request.form['home_address']
            contact = request.form['contact']
            password = request.form['password']
            country = request.form['country']

            # Additional processing logic here

            return 'Signup successful!'
        else:
            return 'Failed to verify reCAPTCHA.', 400

    return render_template("signup.html")

"""
@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        email = request.form.get('email')
        password = request.form.get('password')
        country = request.form.get('country')

        # Generate verification code
        verification_code = generate_verification_code()
        
        # Store user details in the dummy database
        users[email] = {
            'first_name': first_name,
            'last_name': last_name,
            'password': password,
            'country': country,
            'verification_code': verification_code
        }

        # Send verification email
        msg = Message('Verify Your Email', sender='aigbornajohnrpnsamuel.com', recipients=[email])
        msg.body = f'Your verification code is: {verification_code}'
        mail.send(msg)

        flash('A verification code has been sent to your email. Please check and verify.', 'success')
        return redirect(url_for('verify', email=email))

    return render_template('signing.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        email = request.form.get('email')
        verification_code = request.form.get('verification-code')

        # Check if email and verification code match
        if email in users and users[email]['verification_code'] == verification_code:
            # Successful verification, proceed to your desired page
            # Replace 'desired_page_url' with your actual desired page URL
            return redirect(url_for('test'))  # Make sure to define 'desired_page' route
        else:
            flash('Invalid verification code. Please try again.', 'error')

    email = request.args.get('email')
    return render_template('verify.html', email=email)

@app.route('/profile')
# @login_required
def profile():
    return render_template('test.html', current_user=current_user)

"""


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
