# testB Service
######################################    imports and setup    ####################################################
import time
# from common import *

###################################################################################################################
######################################         testB          ###################################################
######################################       SERVICE SETUP       ##################################################
###################################################################################################################
from DNS import MicroXO, WaterSystem, services as water# is_raspberrypi
# Register as a MicroXO Service  (MicroXO is a MicroService Framework)
# This includes a server and clients to communicate with other services
# Naming a class that inherets from MicroXO will allow you to decorate functions with it, and call them from other services

class testB(MicroXO):
	pass



###################################################################################################################
######################################   PUBCIC FUNCTIONS (API)  ##################################################
###################################################################################################################

@testB
def Hello(*args, **kwargs):
	# arduino.reset()
	return {"res": " ::: HELLO! from testB SERVICE !!!", "args": args, "kwargs": kwargs}


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
#######           Robee testB Service            ##########
#######                                             ##########
##############################################################
##############################################################

# Responsibilities:
# 1. 
# 2. 
# 3. 

''')


if __name__ == "__main__":

	test = MicroXO.register("testB", _services = WaterSystem ) 

	if False and is_raspberrypi():
		print(" ::: STARTING testB SERVICE ON RPI!!!!! :::")
		counter = 0
		while True:
			# time.sleep(1)
			print(robee.sensors.realIMU(counter))
			counter += 1
	else:
		print(" ::: STARTING testB SERVICE ON PC!!!!!  :::")
		counter = 0
		while True:
			# time.sleep(1)
			print(robee.testA.mockIMU(counter))
			# print(robee.sensors.testB(counter))
			counter += 1
		
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

