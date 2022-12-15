from MicroXO.mxo import MicroXO

services = MicroXO()

WaterSystem = {
	# "main"           	: {"port":12701, },
	# "webapi"			: {"port": 'http://127.0.0.1:5000/', "serviceType": "socketio"},
	"wapi"		   		: {"port":12701, },
	"Simple"		   	: {"port":12702, },
	"test"		   		: {"port":12710, },
	"testA"		   		: {"port":12711, },
	"testB"		   		: {"port":12712, },
	"status_updater"	: {"port":12713, },
}
services._services = WaterSystem

MicroXO.services = WaterSystem


'''
# To Add a new Service
#  - include it in the WaterSystem Port list


Robbe System OverView
Main Componenets:
- Raspberry Pi (host)
- Arduino - Controls Vehicle, Sensors, etc. Can Run independetly from the RPi
- Sensors - Connected to the arduino
- Interface (Nano) - Managed Through the arduino aswell


'''

def is_raspberrypi():
	import io
	# import os
	try:
		with io.open('/sys/firmware/devicetree/base/model', 'r') as m:
			if 'raspberry pi' in m.read().lower():
				return True
	except Exception:
		pass
	return False




















