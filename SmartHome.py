import serial,urllib,json
import RPi.GPIO as GPIO
from time import sleep
ser = serial.Serial('/dev/ttyACM0', 9600)
s=""
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
def KetNoiServer(url):
	JSON=urllib.urlopen(url)
	data = json.loads(JSON.read())
	n=len(data['list'])
	#print len(data['list'])
	#print 'Lan ',i
	for i in range(0,n):
		#print data['list'][i]['TrangThai']
		#Thiet bi 1
		if data['list'][i]['TrangThai']=='ixp0':
			print 'Bong den 1 tat'
			GPIO.output(5,1)
			continue
		if data['list'][i]['TrangThai']=='ixp1':
			print 'Bong den 1 bat'
			GPIO.output(5,0)
			continue
		#thiet bi 2
		if data['list'][i]['TrangThai']=='aoq0':
			print 'Bong den 2 tat'
			GPIO.output(6,1)
			continue
		if data['list'][i]['TrangThai']=='aoq1':
			print 'Bong den 2 bat'
			GPIO.output(6,0)
			continue
		#thiet bi 3
		if data['list'][i]['TrangThai']=='ukn0':
			print 'Bong den 3 tat'
			GPIO.output(13,1)
			continue
		if data['list'][i]['TrangThai']=='ukn1':
			print 'Bong den 3 bat'
			GPIO.output(13,0)
			continue
		#thiet bi 4
		if data['list'][i]['TrangThai']=='lnd0':
			print 'Bong den 4 tat'
			GPIO.output(19,1)
			continue
		if data['list'][i]['TrangThai']=='lnd1':
			print 'Bong den 4 bat'
			GPIO.output(19,0)
			continue
		#thiet bi 5
		if data['list'][i]['TrangThai']=='vtm0':
			print 'Bong den 5 tat'
			GPIO.output(16,1)
			continue
		if data['list'][i]['TrangThai']=='vtm1':
			print 'Bong den 5 bat'
			GPIO.output(16,0)
			continue
		#thiet bi 6
		if data['list'][i]['TrangThai']=='qry0':
			print 'Bong den 6 tat'
			GPIO.output(26,1)
			continue
		if data['list'][i]['TrangThai']=='qry1':
			print 'Bong den 6 bat'
			GPIO.output(26,0)
			continue
		#thiet bi 7
		if data['list'][i]['TrangThai']=='xhd0':
			print 'Bong den 7 tat'
			GPIO.output(20,1)
			continue
		if data['list'][i]['TrangThai']=='xhd1':
			print 'Bong den 7 bat'
			GPIO.output(20,0)
			continue
		#thiet bi 8
		if data['list'][i]['TrangThai']=='wpv0':
			print 'Bong den 8 tat'
			GPIO.output(21,1)
			continue
		if data['list'][i]['TrangThai']=='wpv1':
			print 'Bong den 8 bat'
			GPIO.output(21,0)
			continue
while True:
	try:
	    data = ser.read()
	    if len(data) > 0:
	        if data!="}":
	            s+=data
	        else:
	            #print s
	            KetNoiServer('http://52.69.6.249/index.php?cmd=laytrangthaiarduino&id=5&nhietdo='+s)
	            s=""
	except KeyboardInterrupt:
		GPIO.cleanup()
		sys.exit()
	except:
		print "Khong co mang"
