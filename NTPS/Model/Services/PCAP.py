def savePacket(Packet, name):
    f = open(name + ".PCAP", "w+")
    f.write(Packet.getAtributes() + "%d\r\n")
    f.close()
    pass

def saveLpacket(Packet):
    f = open("live.PCAP", "w+")
    f.write(Packet.getAtributes() + "\n")
    f.close()
    pass
