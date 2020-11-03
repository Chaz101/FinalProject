import serial
from app import db, login_manager
from datetime import datetime
from sqlalchemy import event
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


@login_manager.user_loader
def load_user(user_id):
	user = teacher.query.get(int(user_id))
	if user:
		return user


class student(db.Model):
	__tablename__ = "student"

	lname = db.Column(db.String(128))
	fname = db.Column(db.String(128))
	id = db.Column(db.Integer, primary_key=True)
	rfid = db.Column(db.String(16))
	present = db.Column(db.String(16))

	def __repr__(self):
		return f"User('{self.id}','{self.lname}','{self.fname}','{self.rfid}','{self.present}')"


class teacher(UserMixin, db.Model):
	__tablename__ = "teacher"

	lname = db.Column(db.String(128))
	fname = db.Column(db.String(128))
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password = db.Column(db.String(128))
	def __repr__(self):
		return f"User('{self.id}','{self.lname}')"

	#def set_password(self, password):
	#	self.password = generate_password_hash(password)

#	def check_password(self, password):
#		return check_password_hash(self.password, password)


@event.listens_for(teacher.password, 'set', retval=True)
def hash_user_password(target, value, oldvalue, initiator):
    if value != oldvalue:
        return generate_password_hash(value)
    return value
