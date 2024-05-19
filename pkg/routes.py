import requests, re, json, datetime, os, string
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort, make_response
from sqlalchemy.sql.functions import current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import text
from markupsafe import escape
from pkg import app, Message, Mail
from pkg.hca_forms import ContactForm, LoginForm, RegisterForm, PasswordResetForm, PasswordResetConfirmForm, VerifyPinForm, EstimatorForm, nigerian_states, user_types
from pkg.models import User, db, Expert, Projects, Forum, Admin, Rating, State, Industry


# @app.errorhandler(CSRFError)
# def csrf_error(e):
# 	return render_template('hca_errors.html', error=e.description), 400


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


def get_user_by_id(uid):
	details = db.session.query(User).get(uid)
	return details


def login_required(x):
	@wraps(x)
	def check_login(*args, **kwargs):
		if session.get('user') is not None:
			return x(*args, **kwargs)
		else:

			flash('you must be logged in to access this page', category='error')
			return redirect('/login/')

	return check_login


# LOGIN
@app.route('/login/', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == 'GET':
		return render_template('login.html', form=form)
	else:
		if form.validate_on_submit():
			email = form.email.data
			pin = form.pin.data
			if email == '' or pin == '':
				flash('Enter registered Details', 'danger')
				return redirect(url_for('login'))
			else:
				user = User.query.filter_by(email=email).first()
				if user is None:
					flash('User does not exist', 'error')
				else:
					stored_pin = user.pin
					check_pin = check_password_hash(stored_pin, pin)
					if check_pin:
						session['user'] = user.username
						return redirect(url_for('profile'))
					else:
						flash('Wrong pin', 'error')
				return redirect('/login/')


# REGISTRATION
@app.route('/register/', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if request.method == 'GET':
		return render_template('register.html', title='HCA|Register', page='register', form=form, states=nigerian_states, user_types=user_types)
	else:
		if form.validate_on_submit():
			username = form.username.data
			email = form.email.data
			first_name = form.first_name.data
			last_name = form.last_name.data
			pin = form.pin.data
			hashed = generate_password_hash(pin)
			mobile = form.mobile.data
			mobile2 = form.mobile2.data
			genders = form.genders.data
			mean_of_identification = form.mean_of_identification.data
			id_number = form.identification_number.data
			company_name = form.company_name.data
			address = form.address.data
			cic = form.cic.data
			dob = form.dob.data
			state = form.state.data
			industry = form.industry.data
			terms = form.terms.data
			file = form.upload_file.data
			registration_date = datetime.datetime.now()

			# TO DATABASE
			user = User(username=username, email=email, first_name=first_name, last_name=last_name, pin=hashed, mobile=mobile, mobile2=mobile2, genders=genders)
			state = State(state=state)
			expert = Expert(username=username, first_name=first_name, last_name=last_name, email=email, pin=hashed, mobile=mobile, mobile2=mobile2, genders=genders,
							mean_of_id=mean_of_identification, company_name=company_name, company_address=address, cic=cic, company_state=state, terms=terms, upload_file=file,
							dob=dob, id_number=id_number, register_date=registration_date)
			industry = Industry(industry=industry)

			db.session.add(user, expert, state, industry)
			db.session.commit()
			flash('Welcome to HCA!', 'success')
			return redirect('/login/')
		else:
			flash('Fill all Fields to Register.', 'danger')
			return render_template('register.html', form=form, title='HCA|Register', page='register', state=nigerian_states)


# PROFILE PAGE
@app.route('/profile/', methods=['GET', 'POST'])
@login_required
def profile():
	uid = session.get('user')
	if id is None:
		details = get_user_by_id(uid)
		return render_template('profile.html', title='HCA|Profile', page='profile', details=details)
	else:
		flash("You must be logged in to access this page", 'error')
		return redirect('/login/')


# LOGOUT
@app.route('/logout/')
def logout():
	if session.get('user') is not None:
		session.pop('user')
	return redirect(url_for('login'))


# CONTACT
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
	if request.method == 'GET':
		return render_template('estimator.html', title='HCA|Estimator', page='estimator', form=form)
	return redirect(url_for('estimator'))


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
