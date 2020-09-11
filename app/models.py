from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash



@login_manager.user_loader
def load_user(user_id):
	user = Student.query.get(int(user_id))
	if user:
		return user
	else:
		return Teacher.query.get(int(user_id))

class Teacher(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	subject = db.Column(db.String(120), index=True)
	def __repr__(self):
		return f"User('{self.id}','{self.subject}')"

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

class Student(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return f"User('{self.id}','{self.username}','{self.email}')"

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

class Subject(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	subname = db.Column(db.String(120), index=True)
	totalclass = db.Column(db.Integer, nullable=True, default=0)

	def __repr__(self):
		return f"User('{self.id}','{self.subname}')"

class Attendance(db.Model):
	id = db.Column(db.Integer, db.ForeignKey('student.id'),primary_key=True, nullable=False)
	subid = db.Column(db.String(10), db.ForeignKey('subject.id'), primary_key=True,nullable=False)
	datemissed = db.Column(db.DateTime, nullable=False, primary_key=True,default=datetime.now())

	def __repr__(self):
		return f"User('{self.id}','{self.subid}','{self.datemissed}')"


