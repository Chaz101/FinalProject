import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERIAL_TIMEOUT = 0
    SERIAL_PORT = 'COM9'
    SERIAL_BAUDRATE = 9600
    SERIAL_BYTESIZE = 8
    SERIAL_PARITY = 'N'
    SERIAL_STOPBITS = 1
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('charliedevwork@gmail.com')
    MAIL_PASSWORD = os.environ.get('CaRIbBeAn1852')
    ADMINS = ['charliedevwork@gmail.com']
    MAIL_DEFAULT_SENDER = ['charliedevwork@gmail.com']
 