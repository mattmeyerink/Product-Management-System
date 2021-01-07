import flask
from . import product_bp
from .models import ProductCategory, Product
from flask_login import login_required, current_user


@product_bp.route("/")
@login_required
def show_product_manager():
    """Display the main product manager page."""
    context = {
        "role": current_user.role,
        "categories": ProductCategory.query.all(),
        "products": Product.query.all()
    }
    return flask.render_template("product_manager.html", **context)

@product_bp.route("/add_product_category", methods=["POST"])
@login_required
def add_product_category():
    """Add a new product category to the db."""
    if flask.request.method == "POST":
        result = flask.request.form
        category = ProductCategory()
        category.from_dict(result)
        category.save()

    return flask.redirect(flask.url_for("products.show_product_manager"))

@product_bp.route("/add_product", methods=["POST"])
@login_required
def add_product():
    """Add a product to the db."""
    if flask.request.method == "POST":
        result = flask.request.form
        product = Product()
        product.from_dict(result)
        product.save()

    return flask.redirect(flask.url_for("products.show_product_manager"))

@product_bp.route("/delete_product/<int:id>")
@login_required
def delete_product(id):
    """Delete a product from the db."""
    product = Product.query.get(id)
    product.remove()

    return flask.redirect(flask.url_for("products.show_product_manager"))
