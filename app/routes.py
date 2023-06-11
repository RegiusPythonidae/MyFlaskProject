from flask import render_template, flash, redirect
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
import os

from app.forms import RegisterForm, ProductForm, LoginForm
from app.modules import app
from app.models import Product, User


user_list = []

@app.route("/")
def index():
    products = Product.query.all()
    discounts = Product.query.filter(Product.price == 600, Product.manufacturer == "AMD").all()
    return render_template("index.html", products=products, discounts=discounts)


@app.route("/add_product", methods=["GET", "POST"])
@login_required
def add_product():

    if not current_user.role == "Admin":
        return redirect("/")

    form = ProductForm()
    if form.validate_on_submit():
        product = Product()
        form.populate_obj(product)
        product.create()
        return redirect('/')

    return render_template("add_product.html", form=form)

@app.route("/edit_product/<int:product_id>", methods=["GET", "POST"])
@login_required
def edit_product(product_id):

    if not current_user.role == "Admin":
        return redirect("/")

    product = Product.query.get(product_id)
    form = ProductForm(obj=product)

    if form.validate_on_submit():
        form.populate_obj(product)
        product.save()
        return redirect("/")
    return render_template("add_product.html", form=form)

@app.route('/delete_product/<int:product_id>')
@login_required
def delete_product(product_id):

    if not current_user.role == "Admin":
        return redirect("/")

    product = Product.query.get(product_id)
    product.delete()
    return redirect("/")

@app.route('/search_product/<string:product_name>')
def search_prpduct(product_name):
    # ყველა დამთხვევის წამოღება
    products = Product.query.filter(Product.name.ilike(f"%{product_name}%")).all()

    # მხოლოდ პირველი დამთხვევის წამოღება
    # products = Product.query.filter(Product.name.ilike(f"%{product_name}%")).first()
    discounts = []
    return render_template("index.html", products=products, discounts=discounts)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.password.data)
        user.create()
    else:
        flash(form.errors)
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        else:
            flash("პაროლი არასწორია")
    else:
        flash(form.errors)
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

# @app.route("/register", methods=["GET", "POST"])
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         new_user = {"username": form.username.data}
#         profile_pic = form.profile_picture.data
#         filename = secure_filename(profile_pic.filename)
#         profile_pic.save(os.path.join(app.root_path, 'static', 'uploads', filename))
#         user_list.append(new_user)
#     else:
#         flash(form.errors)
#     return render_template("register.html", form=form)