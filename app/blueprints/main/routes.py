"""Routes for the homepage."""
import flask
from . import main_bp


@main_bp.route("/")
def show_homepage():
    """Route to display homepage."""
    return flask.render_template("index.html")
