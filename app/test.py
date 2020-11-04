from app.models import student
from app import db
import serial

ser = serial.Serial('COM9')

rfid = ser.readline()
rfid = rfid.decode("utf-8")
rfid = rfid.rstrip('\r\n')
scan = student.query.filter_by(rfid=rfid).first()
scan.present = 'Yes'
db.session.commit()