import serial,urllib,json
from time import sleep
ser = serial.Serial('/dev/ttyACM0', 9600)
s=""
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
			continue
		if data['list'][i]['TrangThai']=='ixp1':
			print 'Bong den 1 bat'
			continue
		#thiet bi 2
		if data['list'][i]['TrangThai']=='aoq0':
			print 'Bong den 2 tat'
			continue
		if data['list'][i]['TrangThai']=='aoq1':
			print 'Bong den 2 bat'
			continue
		#thiet bi 3
		if data['list'][i]['TrangThai']=='ukn0':
			print 'Bong den 3 tat'
			continue
		if data['list'][i]['TrangThai']=='ukn1':
			print 'Bong den 3 bat'
			continue
		#thiet bi 4
		if data['list'][i]['TrangThai']=='lnd0':
			print 'Bong den 4 tat'
			continue
		if data['list'][i]['TrangThai']=='lnd1':
			print 'Bong den 4 bat'
			continue
		#thiet bi 5
		if data['list'][i]['TrangThai']=='vtm0':
			print 'Bong den 5 tat'
			continue
		if data['list'][i]['TrangThai']=='vtm1':
			print 'Bong den 5 bat'
			continue
while True:
    data = ser.read()
    if len(data) > 0:
        if data!="}":
                s+=data
        else:
                #print s
                KetNoiServer('http://52.69.6.249/index.php?cmd=laytrangthaiarduino&id=5&nhietdo='+s)
                s=""