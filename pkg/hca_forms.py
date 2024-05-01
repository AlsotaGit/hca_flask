from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, EmailField, RadioField, SelectField, BooleanField, SubmitField, SelectField, IntegerField, TelField, SelectMultipleField,
                     TextAreaField, HiddenField, FileField, DateField)
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
	email = EmailField('Email', validators=[DataRequired(), Email()])
	pin = PasswordField('Password', validators=[DataRequired(), Length(min=6, message='Password must be at least 6 characters')])
	submit = SubmitField('Log In')


class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[Length(min=3, max=20, message='Username must be between 3 and 20 characters')])
	first_name = StringField('First Name', validators=[DataRequired()])
	last_name = StringField('Last Name', validators=[DataRequired()])
	pin = PasswordField('Pin', validators=[DataRequired(), Length(min=5, message='Pin must be at least 5 characters')])
	confirm_pin = PasswordField('Confirm Pin', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email(), EqualTo('pin'), Email()])
	mobile = TelField('Mobile Number', validators=[DataRequired(), Length(11)])
	mobile2 = TelField('Mobile Number', validators=[Length(11)])
	genders = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
	mean_of_identification = SelectField('Means of Identification', choices=tuple['International Passport', "Driver's licence", 'NIN'], coerce=int, validators=[DataRequired()])
	identification_number = StringField('Identification Number', validators=[DataRequired()])
	dob = DateField('Date of Birth', validators=[DataRequired()])
	upload_file = FileField('Upload File', validators=[DataRequired()])
	company_name = StringField('Company Name', validators=[DataRequired()])
	cic = StringField('CIC No', validators=[DataRequired()])
	address = StringField('Address', validators=[DataRequired()])
	state = StringField('State', validators=[DataRequired()])
	industry = SelectField('Industry', choices=tuple['Industry', 'Mechanical', 'Electrical', 'Construction', 'General labor'], coerce=int)
	specialization = StringField('Specialization/Area of Expertise', validators=[DataRequired()])
	reasons = RadioField('Reason', choices=[('diy', 'DIY Enthusiast|you like to tinker!!'), ('expert', 'Expert/Contractor|improve clientel'), ('both', 'Both|we have got you covered')])
	terms = BooleanField('Agree to terms and conditions', validators=[DataRequired()])
	submit = SubmitField('Register')


class VerifyPinForm(FlaskForm):
	pin = StringField('Pin', validators=[DataRequired(), Length(6, message='Pin must be 6 characters')])
	submit = SubmitField('Verify')


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


class EstimatorForm(FlaskForm):
	units = RadioField(label='Choose Unit', choices=[('metric', 'Metric '), ('imperial', 'Imperial ')], validators=[DataRequired()])
	areas = RadioField('Choose Area', choices=[('concrete', 'Concrete'), ('block_work', 'Block Work'), ('painting', 'Painting'), ('tiling', 'Tiling'),
	('roofing', 'Roofing'), ('plastering', 'Plastering')], validators=[DataRequired()])
	width = IntegerField('Width', validators=[DataRequired()])
	length = IntegerField('Length', validators=[DataRequired()])
	height = IntegerField('Height', validators=[DataRequired()])
	area = IntegerField('Area', validators=[DataRequired()])
	cubic = IntegerField(label='Cubic')
	mix1 = RadioField(label='Standard Mix Ratio:', validators=[DataRequired()])
	mix2 = RadioField(label='Low-Strength Mix:', validators=[DataRequired()])
