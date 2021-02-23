from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

from webapp.main.views import bp as main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.register_blueprint(main_bp)

    return app

app = create_app()