from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

from pkg import config

app.config.from_pyfile('config.py', silent=True)

csrf = CSRFProtect()
csrf.init_app(app)


class Meta:
	csrf = True
	csrf_time_limit = 60 * 60 * 24


from pkg import routes, hca_forms
