from Model.Packet import Packet
from Model.Packet import Layer
from Model.Packet import Field

"""The controller to the packet subsystem. It will do the specified operation based on what 
parameters it has been given."""
def packetController(packet, layerNumber, field, value):
	if (packet == None):                                 # Start/return an empty packet object
		return Packet()
	elif (layerNumber != None and field != None and value != None): # modify field to be value
		packet.modifyPacket(layerNumber, field, value)
	elif (layerNumber != None and field != None):                   # returns the field object
		return packet.provideField(layerNumber, field)
	elif (layerNumber != None):                                     # returns the layer object
		return packet.getLayer(layerNumber)

		
