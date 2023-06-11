from app.modules import db, login_manager

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class BaseModel():
    def create(self):
        db.session.add(self)
        db.session.commit()

    def save(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Product(db.Model, BaseModel):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.Integer, db.ForeignKey("product_types.id"))
    manufacturer = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    price = db.Column(db.Integer)

    type = db.relationship("ProductType")

class ProductType(db.Model, BaseModel):
    __tablename__ = "product_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return self.name

# User Model
class User(db.Model, BaseModel, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)

    def __init__(self, username, password, role="Member"):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)