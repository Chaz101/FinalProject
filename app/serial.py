from app import app, db, ser
from app.models import student


@ser.on_message() #msg is receieved from RFID scan
def handle_message(msg):
	decode = msg.decode('utf-8') #turn RFID UID from a byte into a string
	strip = decode.rstrip('\r\n') #remove extra items from end of string
	print(strip) #print to terminal
	scan = db.session.query(student).filter(student.rfid == strip).first() #checks scanned RFID against any student RFID in database
	print(scan) #prints student to terminal
	if scan.subject == 'None' or scan.present == 'Yes': #if student not meant to be in class OR they are already present, make LED red
		ser.on_send("R")
	else: #If student meant to be in class, make LED blue and change their present status to 'Yes'
		ser.on_send("B")
		scan.present = 'Yes'
		db.session.commit() #Commit change to database
	print(scan) #reprint student to terminal - confirm change