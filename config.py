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
 