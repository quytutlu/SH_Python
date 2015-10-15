import serial,urllib,json
import RPi.GPIO as GPIO
from time import sleep
ser = serial.Serial('/dev/ttyACM0', 9600)
s=""
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Pins=[5,6,13,19,16,26,20,21]
def Init():
        for i in range(0,8):
            GPIO.setup(Pins[i],GPIO.OUT)    
def KetNoiServer(url):
        JSON=urllib.urlopen(url)
        data = json.loads(JSON.read())
        #print len(data['data'])
        n=len(data['data'])
        i=0
        while (i < n):
                #print 'vi tri',i/4,':',data['data'][i+3:i+4]
                tt=0
                if data['data'][i+3:i+4]=='0':
                        tt=1
                GPIO.output(Pins[i/4],tt)
                i=i+4
Init()
while True:
	try:
	    data = ser.read()
	    if len(data) > 0:
	        if data!="}":
	            s+=data
	        else:
	            #print s
	            KetNoiServer('http://smarthometl.com/index.php?cmd=laytrangthaipi&id=5&nhietdo='+s)
	            s=""
	except KeyboardInterrupt:
		GPIO.cleanup()
		sys.exit()
	except:
		print "Khong co mang"
