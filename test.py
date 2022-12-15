# test Service
######################################    imports and setup    ####################################################
import time
# from common import *

###################################################################################################################
######################################         test          ###################################################
######################################       SERVICE SETUP       ##################################################
###################################################################################################################
from DNS import MicroXO, WaterSystem, services as water# is_raspberrypi
# Register as a MicroXO Service  (MicroXO is a MicroService Framework)
# This includes a server and clients to communicate with other services
# Naming a class that inherets from MicroXO will allow you to decorate functions with it, and call them from other services

class test(MicroXO):
	pass



###################################################################################################################
######################################   PUBCIC FUNCTIONS (API)  ##################################################
###################################################################################################################

@test
def hi(*args, **kwargs):
	print("hi!", args, kwargs)
	return "hi!"
	return {"res": " ::: HELLO from WEBAPI SERVICE !!!", "args": args, "kwargs": kwargs}

@test
def Hello(*args, **kwargs):
	# arduino.reset()
	return {"res": " ::: HELLO! from test SERVICE !!!", "args": args, "kwargs": kwargs}


###################################################################################################################
######################################       To be added...      ##################################################
###################################################################################################################



###################################################################################################################
######################################         EXECUTION         ##################################################
###################################################################################################################

print('''
##############################################################
##############################################################
#######                 Bumblebee                   ##########
#######           Robee test Service            ##########
#######                                             ##########
##############################################################
##############################################################

# Responsibilities:
# 1. 
# 2. 
# 3. 

''')

# realIMU = False
# from dal.run_sensors import run as realIMU

test = MicroXO.register("test", _services = WaterSystem ) 

if __name__ == "__main__":
	pass

	# if realIMU and is_raspberrypi():
	# 	print(" ::: STARTING test SERVICE ON RPI!!!!! :::")
	# 	counter = 0
	# 	while True:
	# 		# time.sleep(1)
	# 		print(robee.sensors.realIMU(counter))
	# 		print()
	# 		counter += 1
	# else:
	# 	print(" ::: STARTING test SERVICE ON PC!!!!!  :::")
	# 	counter = 0
	# 	while True:
	# 		# time.sleep(1)
	# 		print(robee.sensors.mockIMU(counter))
	# 		# print(robee.sensors.test(counter))
	# 		counter += 1
		
	# These are available:
	# ard1.Main.Hello("Nice")
	# services.Main.Hello("Nice")
	



# class gps(MicroXO.mxo.MicroXO):
# 	pass


# @gps
# def location(*args, **kwargs):
# 	fin = {"location": {"lat": 37.422, "lng": -122.084}, "args": args, "kwargs":kwargs}
# 	return fin

# gps = MicroXO.mxo.MicroXO.register("gps", _services = WaterSystem ) 

