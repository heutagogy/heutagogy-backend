from heutagogy import app
import os
from datetime import timedelta
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app.config.from_object(__name__)
app.config.update(dict(
    JWT_AUTH_URL_RULE='/api/v1/login',
    JWT_EXPIRATION_DELTA=timedelta(seconds=2592000),  # 1 month

    SECRET_KEY=os.getenv('SECRET_KEY', 'super-secret'),

    # Flask-Mail settings
    USER_ENABLE_EMAIL=int(os.getenv('USER_ENABLE_EMAIL', False)),
    MAIL_USERNAME=os.getenv('MAIL_USERNAME', 'username'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD', 'password'),
    MAIL_DEFAULT_SENDER=os.getenv('MAIL_DEFAULT_SENDER',
                                  'Heutagogy <noreply@no-domain-yet.org>'),
    MAIL_SERVER=os.getenv('MAIL_SERVER', 'smtp.gmail.com'),
    MAIL_PORT=int(os.getenv('MAIL_PORT', '465')),
    MAIL_USE_SSL=int(os.getenv('MAIL_USE_SSL', True)),

    USER_APP_NAME='Heutagogy',
    SQLALCHEMY_DATABASE_URI=os.getenv(
        'DATABASE_URL', 'postgresql:///heutagogy'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False))
app.config.from_envvar('HEUTAGOGY_SETTINGS', silent=True)


if app.config['USER_ENABLE_EMAIL']:
    mail = Mail(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
