"""Class to create models for product categories and products."""
from app import db
from datetime import datetime


class ProductCategory(db.Model):
    __tablename__ = "product_categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    products = db.relationship("Product", cascade="all, delete-orphan", backref="product_categories", lazy=True)

    def __repr__(self):
        return f"<ProductCategory {self.name} | {self.id}>"

    def save(self):
        """Save the current category into the db."""
        db.session.add(self)
        db.session.commit()

    def remove(self):
        """Remove a product category from the db."""
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, data):
        """Populate a product category from a dict."""
        for field in ["name"]:
            if field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        """Output the category to a dictionary."""
        data = {
            "id": self.id,
            "name": self.name,
            "created_on": self.created_on
        }
        return data

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String())
    price = db.Column(db.Float)
    category = db.Column(db.ForeignKey("product_categories.id"))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def _repr__(self):
        return f"<Product {self.name} | {self.id}>"

    def save(self):
        """Save the current product into the db."""
        db.session.add(self)
        db.session.commit()

    def remove(self):
        """Removes a product from the db."""
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, data):
        """Populate a product from a dictionary."""
        for field in ["name", "description", "price", "category"]:
            if field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        """Output the product as a dictionary."""
        data = {
            "id": self.id, 
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category,
            "created_on": self.created_on
        }
