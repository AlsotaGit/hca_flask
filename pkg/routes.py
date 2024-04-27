from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from flask_wtf.csrf import CSRFError
from markupsafe import escape
from pkg import app, csrf
from pkg.hca_forms import ContactForm, LoginForm, RegisterForm, PasswordResetForm, PasswordResetConfirmForm


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
	if form.validate_on_submit():
		return redirect(url_for('profile'))


@app.route('/register/', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		return redirect(url_for('login'))


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
			return redirect(url_for('hca_home', form=form))
	return render_template('contact_us.html', form=form, title='Contact', page='contact')


@app.route('/features/')
def features():
	return render_template('features.html', title='HCA|Features', page='features')


@app.route('/estimator/', methods=['GET', 'POST'])
def estimator():
	return render_template('estimator.html', title='HCA|Estimator', page='estimator')


@app.route('/profile/', methods=['GET', 'POST'])
def profile():
	return render_template('profile.html', title='HCA|Profile', page='profile')


@app.route('/forum/', methods=['GET', 'POST'])
def forum():
	return render_template('forum.html', title='HCA|Forum', page='forum')
