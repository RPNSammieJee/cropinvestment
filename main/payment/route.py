from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required, current_user
from main import db
from main.payment.models import Deposit

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/deposit', methods=['GET', 'POST'])
@login_required
def deposit():
    if request.method == 'POST':
        data = request.form
        
        if not data or 'method' not in data:
            return jsonify({'error': 'Invalid input'}), 400

        amount = 800
        method = data['method']
        
        if amount <= 0:
            return jsonify({'error': 'Invalid deposit amount'}), 400

        if method not in ['bitcoin', 'card']:
            return jsonify({'error': 'Invalid deposit method'}), 400

        # Handle the deposit based on the method
        if method == 'bitcoin':
            print("Bitcoin was chosen")
            pass
        elif method == 'card':
            print("Card was chosen")
            pass
        
        # Add the deposit to the user's balance
        current_user.balance += amount
        db.session.commit()

        # Log the deposit
        deposit = Deposit(type_=method, amount=amount)
        db.session.add(deposit)
        db.session.commit()

        return jsonify({'message': 'Deposit successful', 'new_balance': current_user.balance}), 200

    return render_template('others/deposit.html')

