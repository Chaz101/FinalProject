import os
import secrets
import numpy as np
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, UpdateAccountForm, AttendanceForm, ManualAttendanceForm
from app.models import Student, Teacher, Subject, Attendance
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/", )
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/stlogin", methods=['GET', 'POST'])
def stlogin():
    form = LoginForm()
    if form.validate_on_submit():
        user = Student.query.filter_by(id=form.id.data).first()
        if user and form.password.data==user.password:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('stattendance'))
        else:
            flash('Login Unsuccessful. Please check ID and password', 'danger')
    return render_template('stlogin.html', title='Login', form=form)

@app.route("/flogin", methods=['GET', 'POST'])
def flogin():
    form = LoginForm()
    if form.validate_on_submit():
        user = Teacher.query.filter_by(id=form.id.data).first()
        if user:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('fhome'))
        else:
            flash('Login Unsuccessful. Please check ID and password', 'danger')
    return render_template('flogin.html', title='Login', form=form)

@app.route("/stattendance")
@login_required
def stattendance():
    user = Student.query.filter_by(id=current_user.id).first()
    sublist = Subject.query.all()
    return render_template('stattendance.html', title='About', sublist=sublist)

@app.route("/ftakeattendance", methods=['GET', 'POST'])
@login_required
def ftakeattendance():
    return render_template('ftakeattendance.html', title='About')

@app.route("/fhome")
@login_required
def fhome():
    return render_template('fhome.html', title="choose")

@app.route("/manualadd",methods=['GET','POST'])
@login_required
def manualadd():
    form = ManualAttendanceForm()
    id = form.regid.data
    flash(id)
    return render_template('manualadd.html')

@app.route("/fattendance", methods=['GET', 'POST'])
@login_required
def fattendance():
    form = AttendanceForm()
    form.sub.choices = [(subj.id , subj.subname) for subj in Subject.query.filter_by(fid=current_user.id).all()]
    if request.method == 'POST':
        clist = Subject.query.filter_by(subname=form.sub.data,fid=current_user.id).first()
        course=0
        sem=0
        if clist:
            course = clist.course
            sem = clist.sem
            att = ImageData.query.filter_by(subname=form.sub.data,fid=current_user.id).first()
            if att:
                ImageData.query.filter_by(subname=form.sub.data,fid=current_user.id).delete()
            att = ImageData(subname=form.sub.data,fid=current_user.id)
            db.session.add(att)
            db.session.commit()
        return render_template('ftakeattendance.html', title='Attendance', sub = form.sub.data, course = course, sem = sem)
    return render_template('fattendance.html', form=form)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
       # if form.picture.data:
        #    picture_file = save_picture(form.picture.data)
         #   current_user.image_file = picture_file
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.email.data = current_user.email
   # image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                            form=form)