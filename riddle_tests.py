# Frist tests with RX and TX TCP packets for C180 > https://wiki.maglab.space/wiki/PixelCompetition/C180
# for PixelCompetition on rC3 (remote Chaos Communication Congress)
# Stream https://www.youtube.com/user/jschlingensiepen/live 
# Author: Henning 'haenno' Beier, haenno@web.de (2020)
# License: The Unlicense, https://unlicense.org

# Note: WIP, mostly to send something to the server and see what comes back. Not finished at all. 

import socket
from time import sleep 
import math
import requests
import re

regex = r"RIDDLE (.\d*) (.\d*) (.\d*)"  # c180 

HOST = 'box.pixel-competition.de'
PORT = 2342

def handle_error(error_message):
    print(" ==> ERROR: '"+str(error_message).replace("\n"," ").replace("\r"," ")+"'")
    sleep(0.1)

def drawpixel(x, y, r, g, b):

    while True:
        try:
            ask= ("ASK %d %d\n" % (x,y))
            sock.send(ask.encode())
            sleep(0.5)
            reply = sock.recv(1024)
            print("Riddle: \'" + str(reply).strip() + "\'")
            if not reply:
                break
            matches = re.search(regex, str(reply))
            if matches:
                sqrt_riddle = str(matches.group(3))
                print("Riddle: \'" + sqrt_riddle + "\'")
                break
            break
        except Exception as error_message:
            handle_error(error_message)
            break
    
    #cmd = ('PX %d %d %d %d %d\n' % (y,x,r,g,b))
    #sock.send(cmd.encode())
    

print("Try TCP dialoge...")
while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))

        #getting rid of welcome msg
        #ask= ("help")
        #sock.send(ask.encode())
        #sleep(1)
        #reply = sock.recv(131072)
        #reply = sock.recv(131072)
        #if not reply:
        #    break
        #print ("recvd:\n " + str(reply))


        print("\nCoordinates please... ")
        x = int(input("X? "))
        y = int(input("Y? "))    
        drawpixel(x, y, 245, 255, 0)
        sock.close()
    except Exception as error_message:
        handle_error(error_message)
        break
    
