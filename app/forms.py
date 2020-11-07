from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Regexp
from app.models import teacher, student

#what is displayed on login form
class LoginForm(FlaskForm):
	id = IntegerField('ID Number', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

#what is displayed when updating account
class UpdateAccountForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Update')
	def validate_email(self, email):
		if email.data != current_user.email:
			user = teacher.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('That email is taken. Please choose a different one.')

#what is displayed when adding new students
class AddStudent(FlaskForm):
	fname = StringField('First Name', validators=[DataRequired()])
	lname = StringField('Last Name', validators=[DataRequired()])
	id = IntegerField('Student ID', validators=[DataRequired()])
	rfid = StringField('RFID Tag', validators=[DataRequired()])
	submit = SubmitField('Add Student')

#what is displayed when editing students
class EditStudent(FlaskForm):
	fname = StringField('First Name', validators=[DataRequired()])
	lname = StringField('Last Name', validators=[DataRequired()])
	id = IntegerField('Student ID', validators=[DataRequired()])
	rfid = StringField('RFID Tag', validators=[DataRequired()])
	submit = SubmitField('Edit Student')

