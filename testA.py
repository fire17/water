# testA Service
######################################    other imports and setup    ##############################################
import traceback
# from common import *
import time
from random import random, randint
# import dal.arduino


###################################################################################################################
######################################         testA          ##################################################
######################################       SERVICE SETUP       ##################################################
###################################################################################################################
from DNS import MicroXO, WaterSystem, services as water# is_raspberrypi
# Register as a MicroXO Service  (MicroXO is a MicroService Framework)
# This includes a server and clients to communicate with other services

# Naming a class that inherets from MicroXO will allow you to decorate functions with it, and call them from other services
class testA(MicroXO):
	pass



###################################################################################################################
######################################   PUBCIC FUNCTIONS (API)  ##################################################
###################################################################################################################

@testA
def mockIMU(*args, **kwargs):
	''' Get Mock IMU Data for testings'''
	return {"res":[
		[random(), random(), random(),
		 random()],  # Gyro          (x,y,z,q)
		[random(), random(), random(),
		 random()],  # Accelerometer (x,y,z,q)
		[random(), random(), random(),
		 random()],  # Magnetometer  (x,y,z,q)
	], "time": time.time(),"args": args, "kwargs": kwargs}

@testA
def test(*args, **kwargs):
	return {"res":time.time(),"args": args, "kwargs": kwargs}


###################################################################################################################
######################################       To be added...      ##################################################
###################################################################################################################



############################################ testA ##########################################
############################################ testA ##########################################
############################################ testA ##########################################


###################################################################################################################
######################################         EXECUTION         ##################################################
###################################################################################################################

print('''

##############################################################
##############################################################
#######                 Bumblebee                   ##########
#######           Robee testA Service            ##########
#######                                             ##########
##############################################################
##############################################################

# Responsibilities:
# 1. 
# 2. 
# 3. 

''')

	

test = MicroXO.register("testA", _services=WaterSystem)

if __name__ == "__main__":

	print(" ::: STARTING testA SERVICE ON PC!!!!!  :::",robee._services)

	
	# These are available:
	# ard1.Main.Hello("Nice")
	# services.Main.Hello("Nice")
	
	while True:
		# time.sleep(1)
		print(".",end="")



# class gps(MicroXO.mxo.MicroXO):
# 	pass


# @gps
# def location(*args, **kwargs):
# 	fin = {"location": {"lat": 37.422, "lng": -122.084}, "args": args, "kwargs":kwargs}
# 	return fin

# gps = MicroXO.mxo.MicroXO.register("gps", _services = WaterSystem ) 

