"""Contians function to initialize an instance of the Product Manager System."""
import flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager


# Create an instance of the db
db = SQLAlchemy()

# Initialize Login
login = LoginManager()
login.login_view = 'auth.show_login'

def create_app():
    """Creates an instance of the application."""
    # Initialize the app
    app = flask.Flask(__name__)

    # Add the configuration settings
    app.config.from_object(Config)

    # Link the db to the app
    db.init_app(app)

    # Link the login
    login.init_app(app)

    # Register the blueprints
    from .blueprints.authentication import auth_bp
    app.register_blueprint(auth_bp)

    from .blueprints.main import main_bp
    app.register_blueprint(main_bp)

    from .blueprints.products import product_bp
    app.register_blueprint(product_bp)

    # Create the db
    with app.app_context():
        db.create_all()

    return app

