from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, EmailField, RadioField, SelectField, BooleanField, SubmitField, SelectField, IntegerField,
                     SelectMultipleField, TextAreaField)
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Log In')


class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[Length(min=3, max=20, message='Username must be between 3 and 20 characters')])
	first_name = StringField('First Name', validators=[DataRequired()])
	last_name = StringField('Last Name', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message='Password must be at least 8 characters')])
	confirm_password = PasswordField('Re-Enter Password', validators=[DataRequired(), EqualTo('password')])
	email = StringField('Email', validators=[DataRequired(), Email()])
	mobile = StringField('Mobile Number', validators=[DataRequired(), Length(11)])
	mobile2 = StringField('Mobile Number', validators=[Length(11)])
	submit = SubmitField('Register')


class PasswordResetForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Reset Password')


class PasswordResetConfirmForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired()])
	new_password = PasswordField('New Password', validators=[DataRequired()])
	confirm_password = PasswordField('Re-Enter Password', validators=[DataRequired(), EqualTo('new_password')])
	submit = SubmitField('Reset Password')


class ContactForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	subject = StringField('Subject', validators=[DataRequired()])
	message = TextAreaField('Message', validators=[DataRequired()])
	submit = SubmitField('Send')