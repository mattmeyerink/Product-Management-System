"""Routes for the homepage."""
import flask
from . import main_bp
from flask_login import login_required, current_user


@main_bp.route("/")
@login_required
def show_homepage():
    """Route to display homepage."""
    return flask.redirect("products.show_product_manager")
