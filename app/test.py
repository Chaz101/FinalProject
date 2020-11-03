from app.models import student
from app import db, ser

#ser = serial.Serial('COM9')
ser.open()
ser.flushInput()

while True:
	rfid = ser.readline()
	rfid = rfid.decode("utf-8")
	rfid = rfid.rstrip('\r\n')
	scan = student.query.filter_by(rfid=rfid).first()
	scan.present = 'Yes'
	db.session.commit()