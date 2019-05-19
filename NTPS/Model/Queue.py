


# class will be implemented as a list in order to be able to drop packets from the middle
class Queue:
	__q = []
	__size = 100 # default size of queue should be 100

	# initializer
	def __init__(self, size):
		self.size = size

	# Get the queue size
	def getSize(self):
		return self.size

	# Set the queue size
	def setSize(self, size):
		self.size = size

	# Allow the user the ability to drop a packet from the queue
	def dropPacket(self, packetNumber):
		for x in self.q:
			if(x.getPacketNumber == packetNumber):
				self.q.remove(x)

	# Provide a packet that is stored in the queue to a class that requests it
	def providePacket(self, packetNumber):
		for x in self.q:
			if(x.getPacketNumber == packetNumber):
				return x

	# Adds a packet to the queue
	def addPacket(self, Packet):
		if (self.len < self.size):
			self.q.append(Packet)
		else:
			print("The queue is full")






