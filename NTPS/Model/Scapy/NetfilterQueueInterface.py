import pickle

from netfilterqueue import NetfilterQueue
from Model.Scapy import PypackerInterface


class NetfilterQueueInterface:

    def __init__(self):
        self.nfqueue = NetfilterQueue()
        self.pypacker = PypackerInterface.PypackerInterface()
        pass

    def createPacket(self, packet):
        #print(packet)
        # packet.accept()
        packetBytes = packet.get_payload()
        self.pypacker.extractPacketBytes(packetBytes)
        return packetBytes

    def getPackets(self):
        self.nfqueue.bind(1, self.createPacket)
        try:
            self.nfqueue.run()
        except KeybpardInterrupt:
            print('Error')

        self.nfqueue.unbind()

pass