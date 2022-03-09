from distutils.debug import DEBUG
from os import environ
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://munyao:kevo12@localhost/pitches'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #EMAIL configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    production class
    '''

class DevConfig(Config):
    '''
    development class
    '''
    DEBUG = True

config_options={
    'development': DevConfig,
    'production': ProdConfig
}