import flask
from . import auth_bp


@auth_bp.route("/login")
def show_login():
    """Display the login screen."""
    return flask.render_template("login.html")

@auth_bp.route("/register")
def show_registration():
    """Display the registration page."""
    return flask.render_template("register.html")