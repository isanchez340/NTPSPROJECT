import pickle
from Model.Services.IPtable import disableIptables
from Model.Services.IPtable import enableIptables
from Model.Services.PCAP import saveLpacket
from Model.Services.PCAP import savePacket

def servicesController(packet, name, status):
    if packet is None and name is None:
        if status is 0:
            disableIptables()
        elif status is 1:
            enableIptables()
    elif packet is not None and name is not None:
        savePacket(packet, name)
    elif packet is not None and name is None:
        saveLpacket(packet)
    pass
