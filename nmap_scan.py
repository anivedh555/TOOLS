#!/usr/bin/python3

import nmap
import sys
import socket

target1=str(sys.argv[1])

target=socket.gethostbyname(target1)

ports=[21,22,80,8080,4444,1234,443]

scan_v=nmap.PortScanner()

print('\nScanning',target,'for ports: 21,22,80,8080,4444,1234,443...\n')

for port in ports:
    portscan=scan_v.scan(target,str(port))
    print("Port",port,"is ",portscan['scan'][target]['tcp'][port]['state'])

print("\nHost",target,"is ",portscan['scan'][target]['status']['state'])



