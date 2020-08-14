from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config) #define config.py as app.config

from app import routes