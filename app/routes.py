import os
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, UpdateAccountForm, AddStudent, EditStudent
from app.models import student, teacher
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = teacher.query.filter_by(id=form.id.data).first()
        if user:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('attendance'))
        else:
            flash('Login Unsuccessful. Please check ID and password', 'danger')
    return render_template('login.html', title='Login', form=form)

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

@app.route("/stedit", methods=['GET', 'POST'])
@login_required
def stedit(id):
	user = student.query.filter_by(id=id).first_or_404()
	form = EditStudent()
	if form.validate_on_submit():
		student.lname = form.lname.data
		student.fname = form.fname.data
		student.rfid = form.rfid.data
		db.session.commit()
		flash('Student edited')
		return redirect(url_for('attendance'))
	return render_template('stedit.html', title='Edit Student', form=form)

