from Model.Packet import Field

class Layer:
	"""" attributes from srs
	layerFieldName -will be a string
	layerShowName -will be a string
	layerSize -number
	layerPosition -number
	layerShow -number
	"""
	__layerFieldName = ""
	__layerShowName = ""
	__layerSize = 0
	__layerPosition = -1
	__layerShow = 0
	__fieldList = [] # list of field objects
	
	# initializer
	def __init__(self, layerPosition):
		self.layerPosition = layerPosition
		#self.layerFieldName = layerFieldName

	# add field objects to the layer
	def addField(self, fieldObject):
		self.fieldList.append(fieldObject)

	# provide fields (returns the field object)
	def getField(self, fieldName):
		for x in self.fieldList:
			if (x.getFieldName == fieldName):
				return x
		else: 
			return -1 # field does not exist yet

	"""attribute getters and setters"""
	# layerFieldName setter
	def setLayerFieldName(self, layerFieldName):
		self.layerFieldName = layerFieldName

	# layerFieldName getter
	def getLayerFieldName(self):
		return self.layerFieldName

	# layerShowName setter
	def setLayerShowName(self, layerShowName):
		self.layerShowName = layerShowName

	# layerShowName getter
	def getLayerShowName(self):
		return self.layerShowName

	# layerSize setter
	def setLayerSize(self, layerSize):
		self.layerSize = layerSize

	# layerSize getter
	def getLayerSize(self):
		return self.layerSize

	# layerPosition setter
	def setLayerPostion(self, layerPosition):
		self.layerPosition == layerPosition

	# layerPosition getter
	def getLayerPosition(self):
		return self.layerPosition

	# layerShow setter
	def setLayerShow(self, layerShow):
		self.layerShow = layerShow

	# layerShow getter
	def getLayerShow(self):
		return self.layerShow

	
		
