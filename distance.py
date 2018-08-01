#distance.py
import json
import requests
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 18
GPIO_ECHO = 24
change = False

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Put API URL here for specific storage location
API_ENDPOINT = "https://warm-fortress-76897.herokuapp.com/api/v1/storage_areas/1/storage_locations/1"
#custom header replace token string with proper API_KEY
head = {"Authorization":"Token token=QJmmUGvofbqhkvn2YPbdkmIR2mkVpsgwzk81swqT2/C8cuJR9d68CuBoGoD5DzbKHCRoXPwFxz2IHNBSHr8/EA==, id=1"}
# data to be sent to api
payload = {'storage_location': {'islow': 'true'}}


def distance():
	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)

	StartTime = time.time()
	StopTime = time.time()

	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()

	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()

	TimeElapsed = StopTime - StartTime
	distance = (TimeElapsed * 34300)/2

	return distance

if __name__  == '__main__':
	try:
		while True:
			dist = distance()
			if dist > 10 and change==False:
				# sending post request and saving response as response object
                                r = requests.put(url = API_ENDPOINT, headers=head, json=payload)
                                # extracting response text 
                                response_url = r.text
                                print("The response URL is:%s"%response_url)
                                print(r.url)
                                print ("Resources getting low!")
                                change = True
			elif dist <= 10 and change==True:
                                payload = {'storage_location': {'islow': 'false'}}
                                # sending post request and saving response as response object
                                r = requests.put(url = API_ENDPOINT, headers=head, json=payload)
                                # extracting response text 
                                response_url = r.text
                                print("The response URL is:%s"%response_url)
                                print ("Stock is OK.")
                                change = False
			time.sleep(1500)

	# Reset with ctrl-c		
	except KeyboardInterrupt:
        	print ("Program terminated.")
        	GPIO.cleanup()		
