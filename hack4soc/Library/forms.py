from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from Library.models import User

class RegistrationForm(FlaskForm):
    username = StringField(label = 'Username', validators=[DataRequired(), Length(min=5, max=30)])
    # email = StringField(label = 'Email', validators=[DataRequired(),Email()])
    password1 = PasswordField('Password', validators = [DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm Password', validators = [DataRequired(),EqualTo('password1')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists!')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])    
    password = PasswordField('Password', validators = [DataRequired()])    
    submit = SubmitField('Login')