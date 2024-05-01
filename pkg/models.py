from datetime import datetime

from pkg import db


class Admin(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	password = db.Column(db.String(20), nullable=False)


class User(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	first_name = db.Column(db.String(20), nullable=False)
	last_name = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=True)
	pin = db.Column(db.String(5), nullable=False)
	mobile = db.Column(db.String(20), unique=True, nullable=False)
	mobile2 = db.Column(db.String(20), unique=True, nullable=True)
	gender = db.Column(db.String(20), nullable=False)
	reg_choice = db.Column(db.String(20), nullable=False)
	last_login = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return f"<{self.cust_id}-{self.cust_name}-{self.cust_datereg}>"


class Expert(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	first_name = db.Column(db.String(20), nullable=False)
	last_name = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=True)
	pin = db.Column(db.String(5), nullable=False)
	mobile = db.Column(db.String(20), unique=True, nullable=False)
	mobile2 = db.Column(db.String(20), unique=True, nullable=True)
	gender = db.Column(db.String(20), nullable=False)
	dob = db.Column(db.DateTime, nullable=False)
	reg_choice = db.Column(db.String(20), nullable=False)
	company_name = db.Column(db.String(20), nullable=False)
	company_address = db.Column(db.String(20), nullable=False)
	company_state = db.Column(db.String(20), nullable=False)
	cic = db.Column(db.String(20), nullable=False)
	area_of_specialization = db.Column(db.String(20), nullable=False)
	means_of_id = db.Column(db.String(20), nullable=False)
	id_number = db.Column(db.String(20), nullable=False)
	industry = db.Column(db.String(20), nullable=False)
	register_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	jobs_completed = db.Column(db.Ineger(20), nullable=False)

	def __repr__(self):
		return f"<{self.cust_id}-{self.cust_name}-{self.cust_datereg}>"


class Projects(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String(20), nullable=False)
	description = db.Column(db.String(20), nullable=False)
	category = db.Column(db.String(20), nullable=False)
	project_expert = db.Column(db.Integer, db.ForeignKey('expert.id'), nullable=False)
	project_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	project_cost = db.Column(db.String(20), nullable=False)
	status = db.Column(db.String(20), nullable=False)
	start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	end_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return f"<{self.cust_id}-{self.cust_name}-{self.cust_datereg}>"


class Forum(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	title = db.Column(db.String(20), nullable=False)
	content = db.Column(db.Text, nullable=False)
	author = db.Column(db.String(20), nullable=False)
	create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	update_time = db.Column(db.DateTime, nullable=False, onupdate=datetime.utcnow)

	def __repr__(self):
		return f"<{self.cust_id}-{self.cust_name}-{self.cust_datereg}>"


class Rating(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	expert_id = db.Column(db.Integer, db.ForeignKey('expert.id'), nullable=False)
	rating = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"<{self.cust_id}-{self.cust_name}-{self.cust_datereg}>"
