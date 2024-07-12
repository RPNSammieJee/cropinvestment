from main.auth.route import auth_bp
from main.payment.route import payment_bp
from main.settings.route import setting_bp



def reg_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='/')
    app.register_blueprint(payment_bp, url_prefix='/')
    app.register_blueprint(setting_bp, url_prefix='/')
