# Disco / Warp 
# for PixelCompetition on rC3 (remote Chaos Communication Congress)
# Stream https://www.youtube.com/user/jschlingensiepen/live 
# Author: Henning 'haenno' Beier, haenno@web.de (2020)
# License: The Unlicense, https://unlicense.org

import socket
import random

circle = 10000
lenmax = 1000

def drawpixel(x, y, r, g, b):
    cmd = ('PX %d %d %d %d %d\n' % (x,y,r,g,b))
    sock.send(cmd.encode())

print ("Disco...")

while True:    
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    dist = random.randint(0,lenmax)
    stroke_len = random.randint(20,100)
    stroke_dist = random.randint(40,80)

    print ("-> R %d G %d B %d Dist %d Str-Len %d Str-Abst %d " % (r,g,b,dist,stroke_len,stroke_dist))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('box.pixel-competition.de', 2342))        

    for distance in range (dist,(dist+stroke_dist)):
        for circle_angle in range (1,circle,+stroke_len):
            drawpixel(distance, circle_angle, r, g , b)
    sock.close()

    

