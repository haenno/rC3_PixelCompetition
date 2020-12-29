# Set a new background image.
# for PixelCompetition on rC3 (remote Chaos Communication Congress)
# Stream https://www.youtube.com/user/jschlingensiepen/live 
# Author: Henning 'haenno' Beier, haenno@web.de (2020)
# License: The Unlicense, https://unlicense.org

import socket
import numpy as np
import PIL
from PIL import Image

HOST = 'box.pixel-competition.de'
PORT = 2342

def drawpixel(x, y, r, g, b):

    cmd = ('PX %d %d %d %d %d\n' % (y,x,r,g,b))
    sock.send(cmd.encode())


while True:
    filename = input("Filename? (e.g. 'sample.jpg' - Best resolution is 1920x1080) ->")
    print ("Setting image as new Background...")
    img = Image.open(filename)
    img = img.convert('RGBA')
    arr = np.array(img)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    for i in range(0, img.size[0]):
        for j in range(0, img.size[1]):
          drawpixel(j, i, arr[j][i][0], arr[j][i][1], arr[j][i][2])
    sock.close()
    print("done!")
    
