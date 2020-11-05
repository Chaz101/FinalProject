from flask import Flask
from config import Config
from flask_serial import Serial
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
from flask_migrate import Migrate 
from flask_apscheduler import APScheduler
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(Config) #define config.py as app.config
db = SQLAlchemy(app)
scheduler = APScheduler()
ser = Serial(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes, models, serial
from app.models import teacher, student
from app.routes import AdminTeacher, AdminStudent, AdminIndexView

admin = Admin(app, index_view=AdminIndexView())
admin.add_view(AdminTeacher(teacher, db.session))
admin.add_view(AdminStudent(student, db.session))



