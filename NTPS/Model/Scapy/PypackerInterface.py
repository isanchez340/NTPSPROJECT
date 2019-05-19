import pickle

from pypacker.pypacker import Packet
from pypacker.layer12 import arp, ethernet
from pypacker.layer3 import icmp, ip
from pypacker.layer4 import tcp, udp
from pypacker.layer567 import dns
# import sys

# from Packet.PacketController import *
# import Queue
from Model.Hook.hook import hook

class PypackerInterface:

    def __init__(self):
        # self.queue = Queue()
        # self.packetcontroller = PacketController();
        pass

    def extractPacketBytes(self, packetBytes):
        # packet = self.packetcontroller.packetController()
        ethernetPacket = ethernet.Ethernet(packetBytes)
        #print("%s" % ethernetPacket)
        # self.packetcontroller.packetController(packet, 2)
        for b in str(ethernetPacket):
            pickling_on = open("Emp.pickel", "wb")
            pickle.dump(ethernetPacket[b], pickling_on)
        ipPacket = ip.IP(packetBytes)
        #print("%s" % ipPacket)
        # self.packetcontroller.packetController(packet, 3)
        tcpPacket = tcp.TCP(packetBytes)
        tcpPacket.dissect_full()
        hook.run(tcpPacket)
        print(tcpPacket)
        print("%s" % tcpPacket)
        # self.packetcontroller.packetController(packet, 4)
        # self.queue.addPacket(packet)


pass