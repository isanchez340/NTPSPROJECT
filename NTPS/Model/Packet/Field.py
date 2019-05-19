


class Field:

	""" Attributes from srs
	fieldName -string
	fieldValue -number
	fieldMask -number
	fieldDisplayFormat -string
	"""
	__fieldName = ""
	__fieldValue = 0
	__fieldMask = 0
	__fieldDisplayFormat = ""

	# initializer
	def __init__(self, fieldName, fieldValue):
		self.fieldName = fieldName
		self.fieldValue = fieldValue
	
	"""attribute getters and setters"""
	# fieldName setter
	def setFieldName(self, fieldName):
		self.fieldName = fieldName

	# fieldName getter
	def getFieldName(self):
		return self.fieldName

	# fieldValue setter
	def setFieldValue(self, fieldValue):
		self.fieldValue = fieldValue
			
	# fieldValue getter
	def getFieldValue(self):
		return self.fieldValue

	# fieldMask setter
	def setFieldMask(self, fieldMask):
		self.fieldMask = fieldMask

	# fieldMask getter
	def getFieldMask(self):
		return self.fieldMask

	# fieldDisplayFormat setter
	def setFieldDisplayFormat(self, fieldDisplayFormat):
		self.fieldDisplayFormat = fieldDisplayFormat

	


