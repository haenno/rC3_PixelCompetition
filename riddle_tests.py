# Frist tests with RX and TX TCP packets for C180 > https://wiki.maglab.space/wiki/PixelCompetition/C180
# for PixelCompetition on rC3 (remote Chaos Communication Congress)
# Stream https://www.youtube.com/user/jschlingensiepen/live 
# Author: Henning 'haenno' Beier, haenno@web.de (2020)
# License: The Unlicense, https://unlicense.org

# Note: WIP, mostly to send something to the server and see what comes back. Server (Host and Prt) hardcoded.

import socket
from time import sleep 
from termcolor import colored

def handle_error(error_message):
    print(colored("\n ==> ERROR: ","red"), str(error_message))
    sleep(0.1)

def sndmesg(msg):
    while True:
        try:
            ask= str(msg + "\n")
            sock.send(ask.encode())
            sleep(1)
            reply = sock.recv(1024)
            if not reply:
                handle_error("No Answer!")
            else:
                print("  >> Answer:\n")
                print(colored(reply.decode(), "green"))
            break
        except Exception as error_message:
            handle_error(error_message)
            break

print("A simple dialoge over TCP Sockets...\n > To quit press CTRL+C. \n > Try with asking for 'help' or set a pixel 'PX 100 100 #fff000'... ")

HOST = 'box.pixel-competition.de'
PORT = 2342

try:
    socket.setdefaulttimeout(3.0)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    while True:
        try:
            msg = str(input("\n  >> Message: "))
            sndmesg(msg)
        except Exception as error_message:
            handle_error(error_message)
            break
    sock.close()
except KeyboardInterrupt:
    print(colored("\n\nBye bye...\n","yellow"))
except Exception as error_message:
    handle_error(error_message)
