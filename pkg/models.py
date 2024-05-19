from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Admin(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	password = db.Column(db.String(20), nullable=False)
	last_login = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	current_login = db.Column(db.DateTime, nullable=False, onupdate=datetime.utcnow)


class User(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	first_name = db.Column(db.String(20), nullable=False)
	last_name = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=True)
	pin = db.Column(db.Integer, nullable=False)
	mobile = db.Column(db.String(15), unique=True, nullable=False)
	mobile2 = db.Column(db.String(15), unique=True, nullable=True)
	gender = db.Column(db.String(10), nullable=False)
	reg_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	last_login = db.Column(db.DateTime, nullable=False, onupdate=datetime.utcnow)
	state_id = db.Column(db.Integer, db.ForeignKey('state.id'), nullable=False)
	#  RELATIONSHIPS
	user_expert = db.relationship('Expert', back_populates='expert_user')
	user_projects = db.relationship('Project', back_populates='project_user')
	user_forum = db.relationship('Forum', back_populates='forum_user')
	user_rating = db.relationship('Rating', back_populates='rating_user')
	user_state = db.relationship('State', back_populates='state_user')

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
	company_name = db.Column(db.String(20), nullable=False)
	company_address = db.Column(db.String(20), nullable=False)
	cic = db.Column(db.String(20), nullable=False)
	means_of_id = db.Column(db.String(20), nullable=False)
	id_number = db.Column(db.String(20), nullable=False)
	reg_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	last_login = db.Column(db.DateTime, nullable=False, onupdate=datetime.utcnow)
	jobs_completed = db.Column(db.Integer, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	industry_id = db.Column(db.Integer, db.ForeignKey('industry.id'), nullable=False)
	state_id = db.Column(db.Integer, db.ForeignKey('state.id'), nullable=False)
	# RELATIONSHIPS
	expert_user = db.relationship('User', back_populates='user_expert')
	expert_project = db.relationship('Project', back_populates='project_expert')
	expert_forum = db.relationship('Forum', back_populates='forum_expert')
	expert_rating = db.relationship('Rating', back_populates='rating_expert')
	expert_industry = db.relationship('Industry', back_populates='industry_expert')
	expert_state = db.relationship('State', back_populates='state_expert')

	def __repr__(self):
		return f"<{self.cust_id}-{self.cust_name}-{self.cust_datereg}>"


class Industry(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	industry = db.Column(db.String(20), nullable=False)
	industry_expert = db.relationship('Expert', back_populates='industry_expert')


class State(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	state = db.Column(db.String(20), nullable=False)
	state_user = db.relationship('User', back_populates='user_state')
	state_expert = db.relationship('Expert', back_populates='expert_state')


class Projects(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String(20), nullable=False)
	description = db.Column(db.String(20), nullable=False)
	category = db.Column(db.String(20), nullable=False)
	project_cost = db.Column(db.String(20), nullable=False)
	status = db.Column(db.String(20), nullable=False)
	start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	end_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	project_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	project_expert_id = db.Column(db.Integer, db.ForeignKey('expert.id'), nullable=False)
	project_user = db.relationship('User', back_populates='user_projects')
	project_expert = db.relationship('Expert', back_populates='expert_project')

	def __repr__(self):
		return f"<{self.cust_id}-{self.cust_name}-{self.cust_datereg}>"


class Forum(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	title = db.Column(db.String(20), nullable=False)
	content = db.Column(db.Text, nullable=False)
	author = db.Column(db.String(20), nullable=False)
	create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	update_time = db.Column(db.DateTime, nullable=False, onupdate=datetime.utcnow)
	forum_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	forum_expert_id = db.Column(db.Integer, db.ForeignKey('expert.id'), nullable=False)
	forum_user = db.relationship('User', back_populates='user_forum')
	forum_expert = db.relationship('Expert', back_populates='expert_forum')

	def __repr__(self):
		return f"<{self.cust_id}-{self.cust_name}-{self.cust_datereg}>"


class Rating(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	rating = db.Column(db.Integer, nullable=False)
	rating_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	rating_expert_id = db.Column(db.Integer, db.ForeignKey('expert.id'), nullable=False)
	rating_user = db.relationship('User', back_populates='user_rating')
	rating_expert = db.relationship('Expert', back_populates='expert_rating')

	def __repr__(self):
		return f"<{self.cust_id}-{self.cust_name}-{self.cust_datereg}>"
