import flask
from . import auth_bp
from .models import User, UserRole
from flask_login import login_user, logout_user, current_user
from flask_login import login_required, current_user


@auth_bp.route("/login", methods=["GET", "POST"])
def show_login():
    """Handle Logging into the site"""
    if flask.request.method == "POST":
        # Retrieve the form data from post request
        form_data = flask.request.form.to_dict()
        email = form_data.get("email")
        password = form_data.get("password")

        # Attempt to pull users information from the db
        user = User.query.filter_by(email=email).first()

        # Check if the user in db and password input is correct
        if user and user.check_password_hash(password):
            # Login the user and route them back to the main product page
            login_user(user)
            return flask.redirect(flask.url_for("products.show_product_manager"))

    return flask.render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def show_registration():
    """Display the registration page."""
    if flask.request.method == "POST":
        form_data = flask.request.form.to_dict()
        password = form_data["password"]
        
        user = User()
        user.from_dict(form_data)
        user.hash_password(password)
        user.save()
        return flask.redirect(flask.url_for("products.show_product_manager"))


    return flask.render_template("register.html")

@auth_bp.route("/logout")
def logout():
    """Logout the current user."""
    logout_user()
    return flask.redirect(flask.url_for("authentication.login"))
