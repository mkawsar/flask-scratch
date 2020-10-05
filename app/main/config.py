import os

basedir = os.path.abspath(os.path.dirname(__file__))

POSTGRES = {
    'user': os.getenv('FlASK_POSTGRES_USER', 'root'),
    'pw': os.getenv('FlASK_POSTGRES_PW', 'root'),
    'host': os.getenv('FlASK_POSTGRES_HOST', '127.0.0.1'),
    'port': os.getenv('FlASK_POSTGRES_PORT', '5432'),
    'db': os.getenv('FlASK_POSTGRES_DB', 'flask-scratch'),
}


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_credentials_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
