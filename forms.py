# from wtforms import StringField, PasswordField, BooleanField, SubmitField
# from wtforms.validators import DataRequired, Email, EqualTo
# from flask_wtf import FlaskForm
#
# class LoginForm(FlaskForm):
#     username = StringField("Username", validators=[DataRequired()])
#     password = PasswordField("Password", validators=[DataRequired()])
#     remember_me = BooleanField("Remember me?")
#     submit = SubmitField("Submit")
#
# class RegistrationForm(FlaskForm):
#     username = StringField("Username", validators=[DataRequired()])
#     email = StringField("Email", validators=[DataRequired(), Email()])
#     password = PasswordField("Password", validators=[DataRequired()])
#     password2 = PasswordField(
#         "Repeat Password", validators=[DataRequired(), EqualTo("password")])
#     submit = SubmitField("Register")