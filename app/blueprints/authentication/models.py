"""Models for user authentication including Users and UserRole."""
from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class UserRole(db.Model):
    """Defines the access different users have across the site."""
    __tablename__ = "user_roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    can_add_products = db.Column(db.Boolean())
    can_edit_products = db.Column(db.Boolean())
    can_delete_products = db.Column(db.Boolean())
    can_view_users = db.Column(db.Boolean())
    code = db.Column(db.Integer)
    users = db.relationship("User", cascade="all, delete-orphan", backref="user_roles", lazy=True)

    def __reper__(self):
        return f"<UserRole {self.name}: {self.id}>"

    def save(self):
        """Save the current user role to the db."""
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        """Returns the roles permissions in a dict."""
        data = {
            "id": self.id,
            "name": self.name,
            "can_add_products": self.can_add_products,
            "can_edit_products": self.can_edit_products,
            "can_delete_products": self.can_delete_products,
            "can_view_users": self.can_view_users
        }
        return data

class User(UserMixin, db.Model):
    """Represents a user of the app in the db."""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, index=True)
    password = db.Column(db.String(200))
    role = db.Column(db.ForeignKey("user_roles.id"))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.email}: {self.id}>"

    def save(self):
        """Save the current user to the db."""
        db.session.add(self)
        db.session.commit()

    def remove(self):
        """Remove the current user from the db."""
        db.session.delete(self)
        db.session.commit()

    def hash_password(self, original_password):
        """Hash the input password to store in the db."""
        self.password = generate_password_hash(original_password)

    def check_password_hash(self, original_password):
        """Compare the input password to the hased password in db."""
        return check_password_hash(self.password, original_password)

    def from_dict(self, data):
        """Populate a user object from a dictionary."""
        for field in ["first_name", "last_name", "email", "role"]:
            if field in data:
                setattr(self, field, data[field])
    
    def to_dict(self):
        """Returns a dictionary with the user's information."""
        data = {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "role": self.role,
            "created_on": self.created_on
        }
        return data

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
