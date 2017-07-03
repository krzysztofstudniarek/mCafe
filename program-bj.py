import picamera
import RPi.GPIO as GPIO
import time
import urllib2
import shutil

SENSOR = 21
STATUS = 0 #0 - FREE 1 - BUSY
zmienStatus = False;
zrobFotke = False;

GPIO.setmode (GPIO.BCM)
GPIO.setup (SENSOR,GPIO.IN)

camera = picamera.PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
time.sleep(2)


url = 'http://192.168.43.246:5000/update?status=true&id='
url2 = 'http://192.168.43.246:5000/update?status=false&id='
path = 'server-side-bj/static/'

id = '32e5e5ca-d02b-4d65-9024-6b724183ca52'

while True:
	time.sleep (1)
	sensor_status = GPIO.input(SENSOR)
	if(sensor_status != STATUS):
		start_time = time.time()
		end_time = time.time()
		zmienStatus = True
		while (end_time - start_time) < 0.5:
			print end_time-start_time
			time.sleep(0.01)
			sensor_status = GPIO.input(SENSOR)
			end_time = time.time()
			if(sensor_status == STATUS):
				print 'Przerwana petla'
				zmienStatus = False
				break
		if(zmienStatus):
			STATUS = sensor_status
			zmienStatus = False
			if(STATUS):
				urllib2.urlopen(url2+id).read()
				print 'Robie foto'
				camera.capture('image.jpg')
 
				shutil.copy( path + id + '/image2.jpg', path + id + '/image3.jpg')
				shutil.copy( path + id + '/image1.jpg', path + id + '/image2.jpg')
				shutil.copy('image.jpg', path + id  + '/image1.jpg')
			else:
				urllib2.urlopen(url+id).read()
		



