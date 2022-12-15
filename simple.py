# simple Service
# npx @open-wa/wa-automate --socket -p 8085 -k "0B2FDC9C-FADF48A9-92E5F3D1-D2CDA55A"
# python3 simple.py

# from test import *
# water.Simple.send(number="972543610404", msg="Hello from simple.py")
# water.Simple.send(number="972547932000", msg="Hello from simple.py")

######################################    imports and setup    ####################################################
# Wa Automate Docs: 
# https: // openwa.dev/docs/api/classes/api_Client.Client
from wa_automate_socket_client import SocketClient
import time
from rich.prompt import Prompt

# from common import *
# from dal.utilities.rename_process import set_proc_name
# set_proc_name(b'simple')

###################################################################################################################
######################################         simple          ###################################################
######################################       SERVICE SETUP       ##################################################
###################################################################################################################
from DNS import MicroXO, WaterSystem, services as water# is_raspberrypi
# Register as a MicroXO Service  (MicroXO is a MicroService Framework)
# This includes a server and clients to communicate with other services
# Naming a class that inherets from MicroXO will allow you to decorate functions with it, and call them from other services

class Simple(MicroXO):
	pass


simple = MicroXO.register("Simple", _services=WaterSystem)

simple._groups = {}
simple._apps = {"Google":{"name":" GOOGLE","icon_url":"","description":"Google Search", "invite_link":""}}

@Simple
def setGroupApp(group_id, app, *args, **kwargs):
	if group_id not in simple._groups:
		simple._groups[group_id] = {}
	# if app not in simple._apps:
	# 	simple._apps[app] = {}
	
	simple._groups[group_id]["app"] = app

	# Change group name to app name
	simple._client.setGroupTitle(group_id, simple._apps[app]["name"])
	# simple._client.setGroupIconByUrl(simple._groups[group]["id"], simple._apps[app]["icon_url"])
	# simple._client.setGroupDescription(group_id, simple._apps[app]["description"])
	print("@@@@@@@@@@@@@@@@@@ setGroupApp: ",
	      group_id,simple._apps[app]["name"], simple._apps[app]["description"])
	return True

@Simple
def createGroup(Name = " ::: Test ::: ",participants = ["972543610404@c.us"], *args, **kwargs ):
	print("Creating group: ")
	res = simple._client.createGroup(Name, participants)
	print("Created group: ", res)
	time.sleep(1)
	res2 = simple._client.removeParticipant(res["wid"]["_serialized"], participants[0])
	print("removed participant: ", res2)
	res["invite_link"] = simple._client.getGroupInviteLink(res["wid"]["_serialized"])
	print("invite link: ", res["invite_link"])	
	res["info"] = simple._client.inviteInfo(res["invite_link"])
	print("info : ", res["info"])	
	simple._client.setGroupTitle(res["wid"]["_serialized"], "XXXXXXXXXXXXXXX")
	return res

@Simple
def listGroups(search = "*" , *args, **kwargs):
	res = simple._client.getAllGroups()
	final = {}
	for group in res:
		if search is "*" or search in group["name"]:
			print("group: ", group)
			
			print()
			final[group["id"]] = {"name": group["name"], "id": group["id"],
							 "participants": group["groupMetadata"]["participants"],
							"full_data": group,}
			if "desc" in group["groupMetadata"]:
				final[group["id"]]["desc"] = group["groupMetadata"]["desc"]
			# getGroupInviteLink(group["id"])
			# final[group["id"]] = group
		# elif search in group["name"]:
		# 	final[group["id"]] = group

	for key in final:
		print("key: ", key, " group: ", final[key]["name"], final[key]["id"])
	# print("list groups: ", final)
	return {"groups":final}

	# simple._apps[app] = group

###################################################################################################################
######################################   PUBCIC FUNCTIONS (API)  ##################################################
###################################################################################################################

@Simple
def Hello(*args, **kwargs):
	# arduino.reset()
	return {"res": " ::: HELLO! from simple SERVICE !!!", "client":str(simple._client), "args": args, "kwargs": kwargs}

@Simple
def send(*args, **kwargs):
	# arduino.reset()
	# return {"res": " ::: HELLO! from simple SERVICE !!!", "client":simple._client, "args": args, "kwargs": kwargs}
	# number = Prompt.ask("Enter number to send to")
	number = kwargs["number"] if "number" in kwargs else "972547932000"
	if "@" not in number:
		number = number + "@c.us"
	
	msg = kwargs["msg"] if "msg" in kwargs else "::::::::::::::::\n"+str(kwargs)
	# Executing commands
	return {"res":simple._client.sendText(number, msg)}


@Simple
def test(*args, **kwargs):
	# arduino.reset()
	# return {"res": " ::: HELLO! from simple SERVICE !!!", "client":simple._client, "args": args, "kwargs": kwargs}
	# number = Prompt.ask("Enter number to send to")
	number = kwargs["number"] if "number" in kwargs else "972547932000"
	if "@" not in number:
		number = number + "@c.us"

	msg = kwargs["msg"] if "msg" in kwargs else "::::::::::::::::\n"+str(kwargs)

	# Executing commands
	return {"res": simple._client.sendText(number, msg)}


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
#######           Robee simple Service            ##########
#######                                             ##########
##############################################################
##############################################################

# Responsibilities:
# 1. 
# 2. 
# 3. 

''')

if __name__ == "__main__":

	# These are available:
	# water.logs.info('::: Starting simple Service on port')

	number = '972547932000@c.us'
	secure = "0B2FDC9C-FADF48A9-92E5F3D1-D2CDA55A"
	# secure = "secure_api_key"
	simple._client = SocketClient('http://localhost:8085/', secure)


	def printResponse(message):
		print(" :::",message)


	# Listening for events
	simple._client.onMessage(printResponse)

	# Executing commands
	simple._client.sendText(number, "this is a text")

	# Sync/Async support
	print(" ::: CONNECTED! ",simple._client.getHostNumber())  # Sync request
	# simple._client.sendAudio(NUMBER,
	# 				"https://download.samplelib.com/mp3/sample-3s.mp3",
	# 				sync=False,
	# 				callback=printResponse)  # Async request. Callback is optional

	# Finally disconnect
	# client.disconnect()



# class gps(MicroXO.mxo.MicroXO):
# 	pass


# @gps
# def location(*args, **kwargs):
# 	fin = {"location": {"lat": 37.422, "lng": -122.084}, "args": args, "kwargs":kwargs}
# 	return fin

# gps = MicroXO.mxo.MicroXO.register("gps", _services = WaterSystem ) 

