from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from main import db
from main.settings.models import Setting

setting_bp = Blueprint('setting', __name__)

@setting_bp.route('/setting', methods=['GET', 'POST'])
@login_required
def setting():
    errors = {}
    if request.method == 'POST':
        old_password = request.form.get('old_password')

        if not old_password or not check_password_hash(current_user.password, old_password):
            errors['old_password_error'] = True
            flash('Old password is incorrect.')
            return render_template('pages/setting.html', user=current_user, errors=errors)

        if 'password' in request.form and request.form['password']:
            hashed_password = generate_password_hash(request.form['password'], method='pbkdf2:sha256')
            current_user.password = hashed_password

        if 'phone' in request.form:
            current_user.contact = request.form['phone']

        db.session.commit()
        flash('Settings updated successfully!', 'success')
        return redirect(url_for('setting.setting'))

    return render_template('pages/setting.html', user=current_user, errors=errors)