from Model.Packet import Layer
from Model.Packet import Field

class Packet:
	""" attributes from srs
	packetName -string
	timestamp -time
	"""
	__packetName = "" 
	__timeStamp = 0
	__layerList = [] # list of layers for the packet
	testVariable = 2

	# initializer
	def __init__(self):
		pass

	# add layer objects to the packet
	def addLayer(self, layerObject):
		self.layerList.append(layerObject)

	# filter (by filter we mean get) layer
	def getLayer(self, layerNumber):
		for x in self.layerList:
			if (x.getLayerPosition == layerNumber):
				return x
			else:         # so can tell doesn't exist and can create in modifyPacket
				return -1 
	
	# modify the content of a packet 
	def modifyPacket(layerNumber, field, value, self):
		if (self.getLayer(layerNumber) == -1): # layerNumber doesn't exist so create
			lyr = Layer(layerNumber)
			self.addLayer(lyr)
			if (lyr.getField(field) == -1): # field doesn't exist yet so create
				fld = Field(field, value)
				lyr.addField
		else:   # modifies the field value of the layer
			lyr = self.getLayer(layerNumber)
			fld = lyr.getField(field)
			fld.setFieldValue(value)
			
	# returns the field object
	def provideField(self, layerNumber, field):
		lyr = self.getLayer(layerNumber)
		return lyr.getField(field)
	
	
	"""attribute getters and setters"""
	# packetName setter
	def setPacketName(self, packetName):
		self.packetName = packetName	

	# packetName getter
	def getPacketName(self):
		return self.packetName

	# timeStamp setter
	def setTimeStamp(self, timeStamp):
		self.timeStamp = timeStamp

	# timeStamp getter
	def getTimeStamp(self):
		return self.timeStamp



