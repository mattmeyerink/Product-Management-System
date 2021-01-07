"""Initializes the product bp."""
import flask


product_bp = flask.Blueprint("products", __name__, url_prefix="/products")

from . import routes, models
