#!/bin/bash

cd ~
apt-get install build-essential iptables python3-dev libnetfilter-queue-dev
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
git clone https://github.com/kti/python-netfilterqueue.git
cd python-netfilterqueue
python3 setup.py install
pip3 install pypacker
apt-get install tcpdump
pip3 install --pre scapy[complete]
