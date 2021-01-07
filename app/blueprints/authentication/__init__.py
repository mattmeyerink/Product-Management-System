import flask


auth_bp = flask.Blueprint("auth", __name__, url_prefix="authentication")

import . from routes, models
