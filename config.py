import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://munyao:kevo12@localhost/pitches'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #EMAIL configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")