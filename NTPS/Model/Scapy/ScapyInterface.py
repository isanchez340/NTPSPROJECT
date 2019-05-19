from netfilterqueue import NetfilterQueue
from scapy.all import *

from Model.Scapy.NetfilterQueueInterface import NetfilterQueueInterface


class ScapyInterface:
    netfilter = None

    def __init__(self):
        pass

    def createPackets(self):
        self.netfilter = NetfilterQueueInterface()
        return self.netfilter.getPackets()
        pass

    def forwardPacket(self, packet):

        pass

    def stop(self):
        self.netfilter = None