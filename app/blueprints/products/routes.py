import flask
from . import product_bp
from .models import ProductCategory, Product


@product_bp.route("/")
def show_product_manager():
    """Display the main product manager page."""
    context = {
        "categories": ProductCategory.query.all(),
        "products": Product.query.all()
    }
    return flask.render_template("product_manager.html", **context)

@product_bp.route("/add_product_category", methods=["POST"])
def add_product_category():
    """Add a new product category to the db."""
    if flask.request.method == "POST":
        result = flask.request.form
        category = ProductCategory()
        category.from_dict(result)
        category.save()

    return flask.redirect(flask.url_for("products.show_product_manager"))

@product_bp.route("/add_product", methods=["POST"])
def add_product():
    """Add a product to the db."""
    if flask.request.method == "POST":
        result = flask.request.form
        product = Product()
        product.from_dict(result)
        product.save()

    return flask.redirect(flask.url_for("products.show_product_manager"))

@product_bp.route("/delete_product/<int:id>")
def delete_product(id):
    """Delete a product from the db."""
    product = Product.query.get(id)
    product.remove()

    return flask.redirect(flask.url_for("products.show_product_manager"))
