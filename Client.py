import socket
import sys
import os
import art
import argparse

#Version 1.0 Beta
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
args = parser.parse_args()

MAX_LENGTH = 20000
HOST = args.ipaddress
PORT = args.port
s = socket.socket()
s.connect((HOST, PORT))

while 1:
    msg = input("MT-V2 : ")
    if msg == "close":
        s.close()
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
        print('Recieved')
