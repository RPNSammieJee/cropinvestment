from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from main import db
from main.settings.models import Setting

setting_bp = Blueprint('setting', __name__)


@setting_bp.route('/setting', methods=['GET', 'POST'])
@login_required
def setting():
    if request.method == 'POST':
        if 'password' in request.form and request.form['password']:
            hashed_password = generate_password_hash(request.form['password'], method='pbkdf2:sha256')
            current_user.password = hashed_password

        if 'phone' in request.form:
            current_user.contact = request.form['phone']

        db.session.commit()
        flash('Settings updated successfully!', 'success')
        return redirect(url_for('setting.setting'))

    return render_template('pages/setting.html')
