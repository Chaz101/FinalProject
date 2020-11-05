import os
from time import sleep
from flask import render_template, flash, redirect, url_for, request
from app import app, db, scheduler, ser
from app.forms import LoginForm, UpdateAccountForm, AddStudent, EditStudent
from app.models import student, teacher
from flask_login import login_user, current_user, logout_user, login_required
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import check_password_hash

#Admin panel teachers
class AdminTeacher(ModelView):
	def is_accessible(self):
		return current_user.id == 1
	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('login'))

	column_list = ('id', 'fname', 'lname', 'email')
	column_searchable_list = ('id', 'fname', 'lname', 'email')
#admin panel students
class AdminStudent(ModelView):
	def is_accessible(self):
		return current_user.id == 1
	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('login'))

	column_list = ('id', 'fname', 'lname', 'rfid', 'subject', 'present')
	column_searchable_list = ('id', 'fname', 'lname')
#admin panel homepage (blank)
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
		if user is None or not check_password_hash(user.password, form.password.data):
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


@scheduler.task('cron', id='english_move', hour='9,10,11,12,13,14', minute=30)
def english_move():
	c1 = student.query.filter_by(subject='English').all()
	for c in c1:
		print('Changing subject for '+str(c.fname)+' from '+str(c.subject)+' to maths')
		c.subject = 'Maths'
		c.present = 'No'
	print('Finished')
	db.session.flush()
	db.session.commit()

@scheduler.task('cron', id='maths_move', hour='9,10,11,12,13,14', minute=30)
def maths_move():
	c2 = student.query.filter_by(subject='Maths').all()
	for c in c2:
		print('Changing subject for '+str(c.fname)+' from '+str(c.subject)+' to art')
		c.subject = 'Art'
		c.present = 'No'
	print('Finished')
	db.session.flush()
	db.session.commit()

@scheduler.task('cron', id='art_move', hour='9,10,11,12,13,14', minute=30)
def art_move():
	c3 = student.query.filter_by(subject='Art').all()
	for c in c3:
		print('Changing subject for '+str(c.fname)+' from '+str(c.subject)+' to science')
		c.subject = 'Science'
		c.present = 'No'
	print('Finished')
	db.session.flush()
	db.session.commit()

@scheduler.task('cron', id='science_move', hour='9,10,11,12,13,14', minute=30)
def science_move():
	c4 = student.query.filter_by(subject='Science').all()
	for c in c4:
		print('Changing subject for '+str(c.fname)+' from '+str(c.subject)+' to None')
		c.subject = 'None'
		c.present = 'N/A'
	print('Finished')
	db.session.flush()
	db.session.commit()
	
@scheduler.task('cron', id='none_move', hour='9,10,11,12,13,14', minute=30)
def none_move():
	c5 = student.query.filter_by(subject='None').all()
	for c in c5:
		print('Changing subject for '+str(c.fname)+' from '+str(c.subject)+' to English')
		c.subject = 'English'
		c.present = 'No'
	print('Finished')
	db.session.flush()
	db.session.commit()

scheduler.init_app(app)
scheduler.start()




