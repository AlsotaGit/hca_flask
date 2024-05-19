# SECRET_KEY = 'anykindakey'
# FLASK_APP = 'hca_flask.py'
# FLASK_ENV = 'development'
# FLASK_DEBUG = True

#
class Config(object):
	DATABASE_URI = 'sqlite:///:memory:'
	ADMIN_ID = 'khgdkf2'
	SECRET_KEY = '<securedsecretkey>'


class ProductionConfig(Config):
	DATABASE_URI = 'mysql://user@localhost/hca_flask_test'
	ADMIN_ID = 'kaku1i23kEKu3('
	SECRET_KEY = 'productionsecretkey'


class DevelopmentConfig(Config):
	DATABASE_URI = 'mysql://demo@localhost/hca_flask_test'
	ADMIN_ID = '12Jjk*aJ356'
	SECRET_KEY = 'developsecretkey'


class TestingConfig(Config):
	DATABASE_URI = 'mysql://user@localhost/hca_flask_test'
	ADMIN_ID = 'kaku1i23kEKu3('
	SECRET_KEY = 'testingsecretkey'
	DEBUG = True