from Model.Scapy.ScapyInterface import ScapyInterface

class ScapyController:

    def __init__(self):
        self.scapy = ScapyInterface()
        pass

    def scapyController(self):
        return self.scapy.createPackets()

    def scapyController(self, packet):
        print("This method forwards a packet. :)")
        pass

    def start():
        ScapyInterface().createPackets()

    def stop(self):
        ScapyInterface().stop()
