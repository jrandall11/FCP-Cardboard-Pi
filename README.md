# FCP-Cardboard-Pi
A companion project to FCP Cardboard to monitor storage locations with a Pi distance sensor and alert the application when stock is low

# Instructions
Install python libraries necessary for code to run:

	$ sudo apt-get update
	$ sudo apt-get install rpi.gpio
	$ pipenv install requests

	Set API_ENDPOINT to url of storage location from the API url (/api/v1/storage_areas….)
	Set token in head to the api_key of the storage_location.

	Place Pi at storage location and make sure it has a proper internet connection.
	Run :
		$ sudo python distance.py
 	
	When 	cardboard is depleted to a certain point the distance sensor will trigger.
