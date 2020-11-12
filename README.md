Attendance Project - Robotics & Web Development<br>
Student: Charlie Connor<br>
Teachers: Jim Riley & Julia Tang<br>
README Written: 08/11/2020<br>

-----------------------------

HOW TO INSTALL:
1. Ensure Python3 is downloaded and installed to your system (https://www.python.org/downloads/)<br>
2. Download and unzip the file folder submitted<br>
3. Open your command prompt with WINKEY + R, then type CMD<br>
4. Redirect to the new unziped file folder by typing the following into the CMD:<br>
	cd FOLDER-LOCATION<br>
for example:<br>
	cd C:\Users\School\Desktop\FinalProject<br>
5. Once you are in the final project location, carry out the following command:<br>
	venv\scripts\activate<br>
6. You should now see a (venv) preceeding the command line<br>
7. You'll now need to install the required libraries, use the following command:<br>
	pip install -r requirements.txt<br>
If that doesn't work, try:<br>
	py -m pip install -r requirements.txt<br>
8. All of the packages will install to the venv (virtual environment)<br>
9. Ensure the Arduino is plugged in via USB to the machine<br>
	(The website will still work if the Arduino is not plugged in, however the next step will <br>display an error informing you that it cannot find the USB port)<br>
10. To start the website, run the following:<br>
	flask run<br>
If that doesn't work, try:<br>
	py -m flask run<br>
11. The website will now be hosted on http://localhost:5000/ you can view it at that address<br>

-----------------------------

LOGINS:<br>
You will be prompted to login, there are two logins available and you may create more if required (will be explained later)<br>

Login 1 (admin account):<br>
ID: 1<br>
PW: admin<br>

Login 2 (general teacher acount):<br>
ID: 2<br>
PW: password<br>

-----------------------------

PAGES: <br>
The homepage of this site will list all students, their current class, and their current attendance status. <br>
	Classes are scheduled to change automatically every hour from 09:30 - 14:30. They will only change if the app is running before that time. (for example, if you start the app at 10:29, the classes will all rotate in 1 minute)<br>

There is an Add Student page, here you must fill out all the fields to add a new student to the database. <br>
	They will start off with "None" class and "N/A" present status, however at the scheduled class change time they will be placed into a class with a "No" present status.<br>

There is an account section, here you can just change the user email and view ID. Passwords must be changed by an admin. <br>

You can edit students by clicking on their ID in the homepage. Here you can change their RFID tag, their ID, and name. <br>

You can view the admin panel by manually directing to (http://localhost:5000/admin/). Here you can add new teacher accounts, change passwords, add new students etc. <br>
	Only the admin login (with ID 1) can view this page. This can be edited in the app/routes.py file. <br>

-----------------------------

FILES: <br>
View tree.txt for a full file directory.<br>

Config.py:<br>
This is the configuration of the databases and serial port.<br>

Attendance.py:<br>
This is what the flask run command actually runs. All it does is import from __init__.py<br>

/venv/:<br>
Nothing here should be editied, this is all the installed packages, the pip etc. <br>

/migrations/:<br>
Nothing here should be editied, this is automatically generated folder from the flask-migrations library and it updates whenever there is a database configuration change. <br>

/RFIDScanner/RFIDScanner.ino:<br>
This is where the Arduino code is located. <br>

/app/static/main.css:<br>
This is the CSS I have written to override some of the bootstrap CSS. Most of the CSS and all of the JS is from external sources though. <br>

/app/templates/:<br>
This is where all the HTML files are. They all include base.html as a default. <br>

/app/serial.py:<br>
This is where the serial port is read from Arduino and written to Arduino. <br>

/app/routes.py:<br>
This is where all the web addresses are defined. It will import the HTML files here to redirect when the user completes a task (clicks link, fills password etc).<br>

/app/models.py:<br>
This is where the databases are defined and created<br>

/app/forms.py:<br>
All user forms are included here (add student, login form etc)<br>

/app/__init__.py:<br>
Firs file to run when website is started, initialises the rest of the files and defines resources that are required. <br>


NOTE: <br>
There are only 2 RFID tags included with the project, these tags are attached to the Students Charlie Connor and Glenn Hacket. You will not be able to edit other student present status, unless you change their RFID UID in the edit student page. 


Libraries Used: <br>

https://flask-alembic.readthedocs.io/en/stable/ <br>
https://apscheduler.readthedocs.io/en/stable/faq.html <br>
https://click.palletsprojects.com/en/7.x/ <br>
https://docs.python.org/3/library/datetime.html <br>
https://pypi.org/project/dnspython/ <br>
https://pypi.org/project/email-validator/ <br>
https://flask.palletsprojects.com/en/1.1.x/ <br>
https://flask-admin.readthedocs.io/en/latest/ <br>
https://github.com/viniciuschiele/flask-apscheduler <br>
https://flask-login.readthedocs.io/en/latest/ <br>
https://flask-migrate.readthedocs.io/en/latest/ <br>
https://pypi.org/project/flask-serial/ <br>
https://flask-sqlalchemy.palletsprojects.com/en/2.x/ <br>
https://flask-wtf.readthedocs.io/en/stable/ <br>
https://pypi.org/project/idna/ <br>
https://pypi.org/project/itsdangerous/ <br>
https://jinja.palletsprojects.com/en/2.11.x/ <br>
https://www.makotemplates.org/ <br>
https://pypi.org/project/MarkupSafe/ <br>
https://pythonhosted.org/pyserial/ <br>
https://dateutil.readthedocs.io/en/stable/ <br>
https://pypi.org/project/python-dotenv/ <br>
https://pypi.org/project/pytz/ <br>
https://www.sqlalchemy.org/ <br>
https://docs.python.org/3/library/typing.html <br>
https://pypi.org/project/tzlocal/ <br>
https://werkzeug.palletsprojects.com/en/1.0.x/ <br>
https://wtforms.readthedocs.io/en/2.3.x/ <br>
https://pypi.org/project/zope.interface/ <br>