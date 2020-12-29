# Clears screen with selected color (default: black)
# for PixelCompetition on rC3 (remote Chaos Communication Congress)
# Stream https://www.youtube.com/user/jschlingensiepen/live 
# Author: Henning 'haenno' Beier, haenno@web.de (2020)
# License: The Unlicense, https://unlicense.org

import socket

print("Select color with values for R, G and B from 0-255!\n")
r=int(input("R:"))
g=int(input("G:"))
b=int(input("B:"))

print ("Starting cleanup...")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.connect(('box.pixel-competition.de', 2342))
for x in range (0,1920+1):
    for y in range (0,1080+1):
        cmd = ('PX %d %d %d %d %d\n' % (x,y,r,g,b))
        sock.send(cmd.encode())
sock.close()
print("Done!")
