from wtforms.fields import StringField, PasswordField, SubmitField, SelectField, RadioField, DateField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, length, equal_to
from wtforms import ValidationError
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed

from app.models import User


# class RegisterForm(FlaskForm):
# #
# #     username = StringField("შეიყვანეთ იუზერნეიმი", validators=[DataRequired()])
# #     password = PasswordField("ჩაწერეთ პაროლი", validators=[DataRequired(), length(min=8, max=64)])
# #     repeat_password = PasswordField("გაიმეორეთ პაროლი", validators=[DataRequired(), equal_to("password", message="პაროლები არ ემთხვევა")])
# #     birthday = DateField("დაბადების თარიღი")
# #     about_you = TextAreaField("თქვენს შესახებ")
# #     gender = SelectField("აირჩიეთ სქესი", choices=[(1, "Male"), (2, "Female"), (3, "Other")])
# #     programming_language = RadioField("რომელი ენა იცით", choices=["C#", "Python", "C++"])
# #     profile_picture = FileField("პროფილის სურათი")
# #
# #     register = SubmitField("რეგისტრაცია")
# #
# #     def validate_password(self, field):
# #         if field.data.lower() == field.data:
# #             raise ValidationError("პაროლი უნდა შეიცავდეს დიდ ასოებს")

class RegisterForm(FlaskForm):

    username = StringField("შეიყვანეთ სახელი", validators=[DataRequired()])
    password = PasswordField("შეიყვანეთ პაროლი", validators=[DataRequired()])
    repeat_password = PasswordField("გაიმეორეთ პაროლი", validators=[DataRequired(), equal_to("password")])

    register = SubmitField("რეგისტრაცია")

    def validate_username(self, field):
        user = User.query.filter(User.username == field.data).first()
        if user:
            raise ValidationError("მომხმარებელი უკვე არსებობს")

class LoginForm(FlaskForm):

    username = StringField("შეიყვანეთ სახელი", validators=[DataRequired()])
    password = PasswordField("შეიყვანეთ პაროლი", validators=[DataRequired()])

    login = SubmitField("ავტორიზაცია")

class ProductForm(FlaskForm):

    product_type = SelectField("პროდუქტის ტიპი", choices=[(1, "CPU"), (2, "GPU"), (3, "HDD"), (4, "PSU"), (5, "RAM")])
    manufacturer = StringField("მწარმოებელი")
    name = StringField("პროდუქტის სახელი")
    price = IntegerField("ფასი")

    submit = SubmitField("დამატება")