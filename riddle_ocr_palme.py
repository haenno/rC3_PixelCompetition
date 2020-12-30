# C600 Solution (Riddle OCR Image to text) > https://wiki.maglab.space/wiki/PixelCompetition/C600
# for PixelCompetition on rC3 (remote Chaos Communication Congress)
# Stream https://www.youtube.com/user/jschlingensiepen/live 
# Author: Henning 'haenno' Beier, haenno@web.de (2020)
# License: The Unlicense, https://unlicense.org

# Note: Works, but code is not clean - WIP!

import socket
import numpy as np
import PIL
from time import sleep 
from PIL import Image
import math
import pytesseract
import requests
from io import BytesIO
import re

regex = r"RIDDLE (.\d*) (.\d*) (.*\b.png)"

HOST = 'box.pixel-competition.de'
PORT = 2342


def handle_error(error_message):
    print(" ==> ERROR: '"+str(error_message).replace("\n"," ").replace("\r"," ")+"'")
    sleep(0.1)

def drawpixel(x, y, rgb):
    x = x + 650
    y = y + 750
    while True:
        try:
            ask= ("ASK %d %d\n" % (x,y))
            sock.send(ask.encode())
            #sleep(0.1)
            reply = sock.recv(1024)
            if not reply:
                break
            matches = re.search(regex, str(reply))
            
            if matches:
                url = str(matches.group(3))
                #print("Image URL: \'" + url + "\'")
                try:
                    response = requests.get(url)
                    imgfromurl = Image.open(BytesIO(response.content))
                    riddlestr= pytesseract.image_to_string(imgfromurl)
                    riddlestr = str(riddlestr).strip()
                    print(">Text:       \'" + riddlestr + "\'")
                except Exception as error_message:
                    handle_error(error_message)
                    break
                cmd = ('PX %d %d %s %s\n' % (x,y,rgb,riddlestr))
                sock.send(cmd.encode())
                sleep(0.05)
                reply2 = sock.recv(1024)
                if not reply2:
                    break
                respo = str(reply2.strip())
                print(">Response:   \'" + respo[2:14] +"\'\n")
                
            break
        except Exception as error_message:
            handle_error(error_message)
            break
    

print("One C600 PALME please...")
while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        filename = "palme4.jpg"
        print ("Starting PALME...")
        img = Image.open(filename)
        img = img.convert('RGBA')
        arr = np.array(img)
        for i in range(0, img.size[0]):
            for j in range(0, img.size[1]):
                hex = "#{:02x}{:02x}{:02x}".format(arr[j][i][0], arr[j][i][1], arr[j][i][2])
                drawpixel(j, i, hex)
        sock.close()
    except Exception as error_message:
        handle_error(error_message)    
