import time
from pypacker import interceptor
from pypacker.layer3 import ip,icmp
from pypacker.layer4 import tcp
from pypacker import psocket


def run(pckt):
    pckt.sport = 55555
    pckt.sum = 0
    pckt.dport = 80
    pckt.dst = '8.8.8.8'
    pckt_ip = ip.IP(src_s="127.0.0.1", dst_s="127.0.0.1") + tcp.TCP(dport=80)
    psock = psocket.SocketHndl(mode=psocket.SocketHndl.ETH_P_ALL, timeout=10)
    psock.send(pckt.bin(), pckt_ip.dst_s)
    return