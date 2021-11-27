from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, ValidationError
from .models import User

class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[Email(),DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class PokemonForm(FlaskForm):
    pokemon = StringField('Pokemon Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    first_name= StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[Email(),DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(form, field): #has to be this exactly for email validation
        same_email_user= User.query.filter_by(email= field.data).first() #gives back email from field data of form
        if same_email_user:
            raise ValidationError ("Email is already registered")
        #raise means i am making an error , create an error 