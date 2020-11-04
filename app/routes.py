import os
from flask_apscheduler import APScheduler
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, UpdateAccountForm, AddStudent, EditStudent
from app.models import student, teacher
from flask_login import login_user, current_user, logout_user, login_required
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView


class AdminTeacher(ModelView):
	def is_accessible(self):
		return current_user.id == 1
	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('login'))

	column_list = ('id', 'fname', 'lname', 'email')
	column_searchable_list = ('id', 'fname', 'lname', 'email')

class AdminStudent(ModelView):
	def is_accessible(self):
		return current_user.id == 1
	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('login'))

class AdminIndexView(AdminIndexView):
	def is_accessible(self):
		return current_user.id == 1
	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('login'))       


@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('attendance'))
	form = LoginForm()
	if form.validate_on_submit():
		user = teacher.query.filter_by(id=form.id.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Login Unsuccessful. Please check ID and password', 'danger')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember.data)
		return redirect(url_for('attendance'))
	return render_template('login.html', title='Login', form=form)

@app.route("/", methods=['GET', 'POST'])
@app.route("/attendance")
@login_required
def attendance():
	return render_template('attendance.html', query=student.query.all(), title='Attendance')

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		current_user.email = form.email.data
		db.session.commit()
		flash('Your account has been updated!', 'success')
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form)    

@app.route("/stadd", methods=['GET', 'POST'])
@login_required
def stadd():
	form = AddStudent()
	if form.validate_on_submit():
		s = student(lname=form.lname.data, fname=form.fname.data, id=form.id.data, rfid=form.rfid.data)
		db.session.add(s)
		db.session.commit()
		flash('Student has been added to database')
		return redirect(url_for('stadd'))
	return render_template('stadd.html', title='Add Student', form=form)

@app.route("/stedit/<id>", methods=['GET', 'POST'])
@app.route("/stedit/", methods=['GET', 'POST'])
@login_required
def stedit(id):
	user = student.query.filter_by(id=id).first_or_404()
	form = EditStudent(obj=user)
	if form.validate_on_submit():
		form.populate_obj(user)
		db.session.commit()
		flash('Student edited')
		return redirect(url_for('attendance'))
	return render_template('stedit.html', title='Edit Student', form=form)

scheduler = APScheduler()

@scheduler.task('cron', id='timed_job', hour='9,10,11,12,13,14', minute=38)
def timed_job():
	c1 = student.query.filter_by(subject='English').all().subject = 'Maths'
    c1.subject = 'Maths'
	c2 = student.query.filter_by(subject='Maths').all()
	c2.subject = 'Art'
	c3 = student.query.filter_by(subject='Art').all()
	c3.subject = 'Science'
	print('done')
	
scheduler.init_app(app)
scheduler.start()
