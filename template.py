# template Service
######################################    imports and setup    ####################################################
import time
# from common import *
# from dal.utilities.rename_process import set_proc_name
# set_proc_name(b'template')

###################################################################################################################
######################################         template          ###################################################
######################################       SERVICE SETUP       ##################################################
###################################################################################################################
from DNS import MicroXO, WaterSystem, services as water,# is_raspberrypi
# Register as a MicroXO Service  (MicroXO is a MicroService Framework)
# This includes a server and clients to communicate with other services
# Naming a class that inherets from MicroXO will allow you to decorate functions with it, and call them from other services

class template(MicroXO):
	pass



###################################################################################################################
######################################   PUBCIC FUNCTIONS (API)  ##################################################
###################################################################################################################

@template
def Hello(*args, **kwargs):
	# arduino.reset()
	return {"res": " ::: HELLO! from template SERVICE !!!", "args": args, "kwargs": kwargs}


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
#######           Robee Template Service            ##########
#######                                             ##########
##############################################################
##############################################################

# Responsibilities:
# 1. 
# 2. 
# 3. 

''')

template = MicroXO.register("template", _services = WaterSystem ) 

if __name__ == "__main__":

	# These are available:
	# template.Main.Hello("Nice")
	# water.logs.info('::: Starting Template Service on port')

	while True:
		time.sleep(1)



# class gps(MicroXO.mxo.MicroXO):
# 	pass


# @gps
# def location(*args, **kwargs):
# 	fin = {"location": {"lat": 37.422, "lng": -122.084}, "args": args, "kwargs":kwargs}
# 	return fin

# gps = MicroXO.mxo.MicroXO.register("gps", _services = WaterSystem ) 

