import os
def disableIptables():
    os.system("sudo iptables-save > /root/firewall.rules")
    os.system("iptables -X")
    os.system("iptables -t nat -F")
    os.system("iptables -t nat -X")
    os.system("iptables -t mangle -F")
    os.system("iptables -t mangle -X")
    os.system("iptables -P INPUT ACCEPT")
    os.system("iptables -P FORWARD ACCEPT")
    os.system("iptables -P OUTPUT ACCEPT")
    os.system("iptables -I INPUT -j NFQUEUE --queue-num 1")
    pass

def enableIptables():
    os.system("iptables-restore < /root/firewall.rules")
    pass

enableIptables()