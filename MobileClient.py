import socket
import sys
import os
import argparse

#Version 1.2
#Adaptaion YenisFish-Adaptation-Mobile

print('Welcome To MightyTripV2 Mobile')
print('This version of MightyTrip V2 is still in Beta, there are many bugs and security risks!')
print('MightyTrip V2 is a Client to Server socket program for remote use of Terminals.')
print('This is an adaptation of MightyTrip by Psyonik and YendisFish')
print('Created by: YendisFish')

MAX_LENGTH = 50000
HOST = input('Host > ')
PORT = input('Port > ')
s = socket.socket()
s.connect((HOST, int(PORT))

while True:
    msg = input("MT-V2 : ")
    if msg == "close":
        print('Attempting to close socket')
        s.close()
        print('Successfully Closed Socket')
        print('Terminating Program')
        sys.exit(0)
    try:
        s.send(msg.encode("utf-8"))
        data = s.recv(MAX_LENGTH).decode("utf-8")
        topcover = print('==========Data==========')
        dataout = print(data)
        bottomcover = print('------------------------')
    except:
        print(msg)
        line = 44

