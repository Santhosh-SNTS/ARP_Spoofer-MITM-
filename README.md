# ARP_Spoofer-MITM

What is ARP Spoofing (ARP Poisoning)
An ARP spoofing, also known as ARP poisoning, is a Man in the Middle (MitM) attack that allows attackers to intercept communication between network devices. The attack works as follows:

1. The attacker must have access to the network. They scan the network to determine the IP addresses of at least two devices⁠—let’s say these are a workstation and a router. 
2. The attacker uses a spoofing tool, such as Arpspoof or Driftnet, to send out forged ARP responses. 
3. The forged responses advertise that the correct MAC address for both IP addresses, belonging to the router and workstation, is the attacker’s MAC address. This fools both router and workstation to connect to the attacker’s machine, instead of to each other.
4. The two devices update their ARP cache entries and from that point onwards, communicate with the attacker instead of directly with each other.
5. The attacker is now secretly in the middle of all communications.

*TO RUN THIS TOOL*

step1: download and install scapy module 
       
       pip install --pre scapy[complete]
 or download and install scapy module 
       
       https://github.com/secdev/scapy
 To install : Move to that directory using terminal, 
 then cmd: 
         
       python setup.py install 

step2: Move to our tool location

serp3: If python 2.7
      
      python arp_spoofer2.py   
  If pyhton 3.8 or 3.9 
      
      python3 arp_spoofer3.py
step4: Enter the target IP you want to spoof eg: 192.168.225.22 

step5: Enter the Router IP to be Man in the Middle eg: 192.168.225.1


To close this program press ctrl+c
