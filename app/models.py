from app import db
from datetime import datetime

class Admin(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return '<Admin {}>'.format(self.username)

class Teacher(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return '<Teacher {}>'.format(self.username)

class Student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return '<Student {}>'.format(self.username)

class classroom(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	classes = db.Column(db.String(64), index=True)
	Teacher = db.Column(db.Integer, db.ForeignKey('teacher.id'))
	Students = db.Column(db.Integer, db.ForeignKey('student.id'))

	def __repr__(self):
		return '<classroom {}>'.format(self.classes)

