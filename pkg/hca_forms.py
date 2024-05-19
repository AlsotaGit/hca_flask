from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, EmailField, RadioField, SelectField, BooleanField, SubmitField, SelectField, IntegerField, TelField, SelectMultipleField,
                     TextAreaField, HiddenField, FileField, DateField)
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

nigerian_states = [
	("Abia", "Abia"), ("Adamawa", "Adamawa"), ("Akwa Ibom", "Akwa Ibom"), ("Anambra", "Anambra"), ("Bauchi", "Bauchi"),
	("Bayelsa", "Bayelsa"), ("Benue", "Benue"), ("Borno", "Borno"), ("Cross River", "Cross River"), ("Delta", "Delta"),
	("Ebonyi", "Ebonyi"), ("Edo", "Edo"), ("Ekiti", "Ekiti"), ("Enugu", "Enugu"), ("Gombe", "Gombe"), ("Imo", "Imo"),
	("Jigawa", "Jigawa"), ("Kaduna", "Kaduna"), ("Kano", "Kano"), ("Katsina", "Katsina"), ("Kebbi", "Kebbi"), ("Kogi", "Kogi"),
	("Kwara", "Kwara"), ("Lagos", "Lagos"), ("Nasarawa", "Nasarawa"), ("Niger", "Niger"), ("Ogun", "Ogun"), ("Ondo", "Ondo"),
	("Osun", "Osun"), ("Oyo", "Oyo"), ("Plateau", "Plateau"), ("Rivers", "Rivers"), ("Sokoto", "Sokoto"), ("Taraba", "Taraba"),
	("Yobe", "Yobe"), ("Zamfara", "Zamfara"), ("Federal Capital Territory", "Federal Capital Territory")
]

identification_means = [
	("National ID Card", "National ID Card"),
	("International Passport", "International Passport"),
	("Driver's License", "Driver's License"),
	("Permanent Voter's Card", "Permanent Voter's Card"),
]

construction_sections = [
	("Industry", "Industry"),
	("Mechanical", "Mechanical"),
	("Electrical", "Electrical"),
	("Construction", "Construction"),
	("General labor", "General labor")
]

user_types = [
	("diy", "DIY Enthusiast|ou like to tinker!!"),
	("expert", "Expert/Contractor|Improve clientele"),
	("both", "Both|We've got you covered")
]

construction_activities = [
	("concrete", "Concrete"),
	("block_work", "Block Work"),
	("painting", "Painting"),
	("tiling", "Tiling"),
	("roofing", "Roofing"),
	("plastering", "Plastering")
]

block_sizes = [
	(9, '9 inch'),
	(6, '6 inch')
]


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
	mean_of_identification = SelectField('Means of Identification', choices=identification_means, validators=[DataRequired()])
	identification_number = StringField('Identification Number', validators=[DataRequired()])
	dob = DateField('Date of Birth', validators=[DataRequired()])
	upload_file = FileField('Upload File', validators=[DataRequired()])
	company_name = StringField('Company Name', validators=[DataRequired()])
	cic = StringField('CIC No', validators=[DataRequired()])
	address = StringField('Address', validators=[DataRequired()])
	state = SelectField('State', choices=nigerian_states, validators=[DataRequired()])
	industry = SelectField('Industry', choices=construction_sections, validators=[DataRequired()])
	reasons = RadioField('Reason', choices=user_types, validators=[DataRequired()])
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
	units = RadioField('Choose Unit', choices=[('metric', 'Metric '), ('imperial', 'Imperial ')], validators=[DataRequired()])
	areas = RadioField('Choose Area', choices=construction_activities, validators=[DataRequired()])
	width = IntegerField('Width', validators=[DataRequired()])
	length = IntegerField('Length', validators=[DataRequired()])
	height = IntegerField('Height', validators=[DataRequired()])
	area = IntegerField('Area', validators=[DataRequired()])
	block = RadioField('Size of Block', choices=block_sizes, validators=[DataRequired()])
	cubic = IntegerField('Cubic')
	mix1 = RadioField('Standard Mix Ratio:', validators=[DataRequired()])
	mix2 = RadioField('Low-Strength Mix:', validators=[DataRequired()])
