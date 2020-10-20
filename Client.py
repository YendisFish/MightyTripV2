import socket
import sys
import os
import art
import argparse

#Version 1.6
#Adaptaion YenisFish-Adaptation

""" COLORS """


def prRed(skk): print("\033[91m {}\033[00m".format(skk))
def prGreen(skk): print("\033[92m {}\033[00m".format(skk))
def prYellow(skk): print("\033[93m {}\033[00m".format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m".format(skk))
def prPurple(skk): print("\033[95m {}\033[00m".format(skk))
def prCyan(skk): print("\033[96m {}\033[00m".format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m".format(skk))
def prBlack(skk): print("\033[98m {}\033[00m".format(skk))

os.system('cls')
os.system('color A')
art.tprint("Mighty-Trip V2", font="random")
prRed('This version of MightyTrip V2 is still in Beta, there are many bugs and security risks!')
prPurple('MightyTrip V2 is a Client to Server socket program for remote use of Terminals.')
prRed('This is an adaptation of MightyTrip by Psyonik and YendisFish')
prPurple('Created by: YendisFish')

parser = argparse.ArgumentParser(description="MightyTripV2")
parser.add_argument('-i', '--ipaddress', help='Server IP Address', required=True)
parser.add_argument('-p', '--port', help='Server Port', type=int, default=10544)
parser.add_argument('-os', help='OS input', default='linux', required=True)
parser.add_argument('-pac-size', help='Change packet size', default=50000)
args = parser.parse_args()

OS = args.os
MAX_LENGTH = args.pac_size
prGreen('Packet size set to ' + MAX_LENGTH)
HOST = args.ipaddress
PORT = args.port
s = socket.socket()
s.connect((HOST, PORT))

print('Starting Client for ' + OS)

if OS == 'mac':
    print('Welcome Mac User!')
    prYellow('WARNING: MightyTripV2 is native to linux and may not work as well on Mac OS')

if OS == 'linux':
    prYellow('Welcome Superior Being')

if OS == 'windows':
    prYellow('WARNING: Although with more working features, the windows version of MightyTripV2 isnt the best version to use due to security issues')

while 1:
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
