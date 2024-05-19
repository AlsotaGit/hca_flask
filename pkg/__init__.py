# from flask import Flask
# from flask_wtf.csrf import CSRFProtect
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from pkg import config
#
# app = Flask(__name__, instance_relative_config=True)
#
# app.config.from_pyfile('config.py', silent=True)
#
# if app.config['ENV'] == 'development':
# 	app.config.from_object(config.DevelopmentConfig)
# else:
# 	app.config.from_object(config.ProductionConfig)
#
# db = SQLAlchemy(app)  # INSTANTIATE
#
# migrate = Migrate(app, db)  # TRYING TO CONNECT APP ND DB
#
# csrf = CSRFProtect()
# csrf.init_app(app)
#
#
# class Meta:
# 	csrf = True
# 	csrf_time_limit = 60 * 60 * 24
#
#
# from pkg import routes, hca_forms, models


from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from flask_mail import Mail, Message

csrf = CSRFProtect()

mail = Mail()


def create_app():
	from pkg.models import db
	from pkg import config
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_pyfile('config.py', silent=True)
	app.config.from_object(config.TestingConfig)
	db.init_app(app)
	csrf.init_app(app)
	mail.init_app(app)
	migrate = Migrate(app, db)
	return app


app = create_app()
from pkg import routes, hca_forms
