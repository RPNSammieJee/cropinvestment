from .auth.route import auth_bp


def reg_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='/')
