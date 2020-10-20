import socket
import sys
import os
import art
import argparse

#Version 1.8
#Adaptaion YenisFish-Adaptation

class colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

os.system('cls')
os.system('color A')
art.tprint("Mighty-Trip V2", font="random")
print(colors.RED + 'This version of MightyTrip V2 is still in Beta, there are many bugs and security risks!')
print(colors.PURPLE + 'MightyTrip V2 is a Client to Server socket program for remote use of Terminals.')
print(colors.RED + 'This is an adaptation of MightyTrip by Psyonik and YendisFish')
print(colors.PURPLE + 'Created by: YendisFish')

parser = argparse.ArgumentParser(description="MightyTripV2")
parser.add_argument('-i', '--ipaddress', help='Server IP Address', required=True)
parser.add_argument('-p', '--port', help='Server Port', type=int, default=10544)
parser.add_argument('-os', help='OS input', default='linux', required=True)
args = parser.parse_args()

OS = args.os
MAX_LENGTH = 50000
HOST = args.ipaddress
PORT = args.port
s = socket.socket()
s.connect((HOST, PORT))

print('Starting Client for ' + OS)

if OS == 'mac':
    print('Welcome Mac User!')
    print(colors.YELLOW + 'WARNING: MightyTripV2 is native to linux and may not work as well on Mac OS')

if OS == 'linux':
    print(colors.YELLOW + 'Welcome Superior Being')

if OS == 'windows':
    print(colors.YELLOW + 'WARNING: Although with more working features, the windows version of MightyTripV2 isnt the best version to use due to security issues' + colors.END)

while 1:
    msg = input(colors.BOLD + colors.GREEN + "MT-V2 : " + colors.END + colors.PURPLE)
    colors.END
    if msg == "close":
        print(colors.RED + 'Attempting to close socket')
        s.close()
        print(colors.GREEN + 'Successfully Closed Socket')
        print(colors.RED + 'Terminating Program')
        sys.exit(0)
    try:
        s.send(msg.encode("utf-8"))
        data = s.recv(MAX_LENGTH).decode("utf-8")
        topcover = print(colors.CYAN + '==========Data==========')
        dataout = print(colors.BLUE + colors.BOLD + data)
        bottomcover = print(colors.CYAN + '------------------------')
    except:
        print(msg)
        line = 44
