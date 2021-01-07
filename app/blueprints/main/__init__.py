"""Blueprint for homepage."""
import flask


main_bp = flask.Blueprint("main", __name__, url_prefix="")

from . import routes