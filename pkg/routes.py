from flask import Flask, render_template, request, redirect, url_for, session, flash, abort, make_response
from flask_wtf.csrf import CSRFError
from sqlalchemy.sql import text
from markupsafe import escape
from pkg import app, csrf
from pkg.hca_forms import ContactForm, LoginForm, RegisterForm, PasswordResetForm, PasswordResetConfirmForm, VerifyPinForm, EstimatorForm
from pkg.models import User


@app.errorhandler(CSRFError)
def csrf_error(e):
	return render_template('hca_errors.html', error=e.description), 400


@app.errorhandler(404)
def page_not_found(e):
	return render_template('hca_errors.html', error=e), 404


@app.errorhandler(410)
def page_gone(e):
	return render_template('hca_errors.html', error=e), 410


@app.errorhandler(500)
def server_error(e):
	return render_template('hca_errors.html', error=e), 500


@app.route('/')
def hca_home():
	return render_template('index.html', title='HCA|Home', page='hca')


@app.route('/login/', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			email = form.email.data
			password = form.password.data
			if email == email and password == password:
				session['email'] = email
				flash('You are now logged in!', 'success')
				return render_template('profile.html')
			else:
				flash('Please enter your email and password.')
	return render_template('login.html', form=form, title='HCA|Login', page='login')


@app.route('/register/', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			# username = form.username.data
			# email = form.email.data
			# password = form.password.data
			# confirm_password = form.confirm_password.data
			# first_name = form.first_name.data
			# last_name = form.last_name.data
			# pin = form.pin.data
			# confirm_pin = form.confirm_pin.data
			# mobile = form.mobile.data
			# mobile2 = form.mobile2.data
			# genders = form.genders.data
			# mean_of_identification = form.mean_of_identification.data
			# company_name = form.company_name.data
			# address = form.address.data
			# cic = form.cic.data
			# state = form.state.data
			# industry = form.industry.data
			# specialization = form.specialization.data
			# reasons = form.reasons.data
			# terms = form.terms.data
			# file = form.upload_file.data
			flash('Welcome to HCA!', 'success')
			return render_template('login.html')
		else:
			flash('Please enter your email and password.')
			return render_template('register.html', form=form, title='HCA|Register', page='register')
	return render_template('register.html', form=form, title='HCA|Register', page='register')


@app.route('/logout/')
def logout():
	session.clear()
	return redirect(url_for('login'))


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if form.validate_on_submit():
		email = form.email.data
		subject = form.subject.data
		message = form.message.data
		if email == '' and subject == '' and message == '':
			return render_template('contact_us.html')
		else:
			flash('Thank you for contacting HCA!', 'success')
			return render_template('index.html')
	return render_template('contact_us.html', form=form, title='Contact', page='contact')


@app.route('/features/')
def features():
	return render_template('features.html', title='HCA|Features', page='features')


@app.route('/estimator/', methods=['GET', 'POST'])
def estimator():
	form = EstimatorForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			units = form.units.data
			areas = form.areas.data
			return render_template('estimator.html', units=units, areas=areas, title='HCA|Estimator', page='estimator', form=form)
	return render_template('estimator.html', title='HCA|Estimator', page='estimator', form=form)


@app.route('/profile/', methods=['GET', 'POST'])
def profile():
	username = 'johndoe'
	name = 'John'
	email = 'johdoe@gm.com'
	mobile = '+2348095232846'
	return render_template('profile.html', username=username, name=name, email=email, mobile=mobile, title='HCA|Profile', page='profile')


@app.route('/forum/', methods=['GET', 'POST'])
def forum():
	return render_template('forum.html', title='HCA|Forum', page='forum')


@app.route('/verification/', methods=['GET', 'POST'])
def verification():
	form = VerifyPinForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			pin = form.pin.data
			if pin == '123456':
				flash('Verification code is correct.', 'success')
				return redirect(url_for('hca_home'))
			else:
				flash('invalid Verification code', 'danger')
	return render_template('verification.html', form=form, title='HCA|Verification', page='verification')
