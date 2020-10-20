import socket
import sys
import os
import argparse

#Version 1.0
#Adaptaion YenisFish-Adaptation-Mobile

""" COLORS """


def prRed(skk): print("\033[91m {}\033[00m".format(skk))
def prGreen(skk): print("\033[92m {}\033[00m".format(skk))
def prYellow(skk): print("\033[93m {}\033[00m".format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m".format(skk))
def prPurple(skk): print("\033[95m {}\033[00m".format(skk))
def prCyan(skk): print("\033[96m {}\033[00m".format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m".format(skk))
def prBlack(skk): print("\033[98m {}\033[00m".format(skk))


prGreen('Welcome To MightyTripV2 Mobile')
prRed('This version of MightyTrip V2 is still in Beta, there are many bugs and security risks!')
prPurple('MightyTrip V2 is a Client to Server socket program for remote use of Terminals.')
prRed('This is an adaptation of MightyTrip by Psyonik and YendisFish')
prPurple('Created by: YendisFish')

MAX_LENGTH = 50000
HOST = input('Host > ')
PORT = input('Port > ')
s = socket.socket()
s.connect((HOST, int(PORT))

while True:
    msg = input("MT-V2 : ")
    if msg == "close":
        prRed('Attempting to close socket')
        s.close()
        prGreen('Successfully Closed Socket')
        prRed('Terminating Program')
        sys.exit(0)
    try:
        s.send(msg.encode("utf-8"))
        data = s.recv(MAX_LENGTH).decode("utf-8")
    except:
        print(msg)
        line = 44
    theydata = prCyan('--------------------')
    dodata = print(data)
    datacolor = prCyan('--------------------')
    if msg == "dir":
        prCyan(data)
    if msg == "ping":
        prRed(data)
    if msg == "arp -a":
        prPurple(data)
    if msg == "help":
        msg = os.system('help')
    if msg == "help":
        prRed(data)
    if msg == 'Help':
        prRed(data)
    if data == 'failed':
        line = 16
        prGreen('Received')