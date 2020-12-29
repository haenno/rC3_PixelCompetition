# CCC bzw. Chaos-Siegen / Hasi bzw. Hackspace Siegen Palme 
# for PixelCompetition on rC3 (remote Chaos Communication Congress)
# Stream https://www.youtube.com/user/jschlingensiepen/live 
# Author: Henning 'haenno' Beier, haenno@web.de (2020)
# License: The Unlicense, https://unlicense.org

from time import sleep,time
import threading
import socket
import numpy as np
import PIL
from PIL import Image
import random

def handle_error(error_message):
    print(" ==> ERROR: '"+str(error_message).replace("\n"," ").replace("\r"," ")+"'")
    sleep(0.1)

def write_to_console(message):
    print(str(message).rstrip())
    sleep(0.1)

def make_new_palm():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1.0)
        result = sock.connect_ex(('box.pixel-competition.de', 2342))
        if result == 0:
            offset_y = 20
            offset_x = 1500
            for x in range(0, img.size[0]):
                for y in range(0, img.size[1]):
                    cmd = ('PX %d %d %d %d %d\n' % ((x + offset_x),(y + offset_y),arr[y][x][0],arr[y][x][1],arr[y][x][2]))
                    sock.send(cmd.encode())
        sock.close()
    except Exception as error_message:
        handle_error(error_message)

def palme():
    loop_timeout = time() + 15
    write_to_console("New PALMEN...")
    for i in range(1,4): 
        write_to_console("  ...>> Starting single PALME " + str(i))
        threading.Thread(target=make_new_palm).start()
        sleep(3)
    while threading.active_count() != 1: 
        write_to_console(" > Remaing PALMEN: "+ str(threading.active_count()-1))
        sleep(1.5)        
        if time() > loop_timeout:
            write_to_console("...PALMEN timelimit hit, starting next PALMEN.")
            return "timeout"
    write_to_console("...PALMEN done.")
    return "ok"

img = Image.open('zement_palme.jpg')
img = img.convert('RGBA')
arr = np.array(img)

while True:
    try:
        palme()
    except Exception as error_message:
        handle_error(error_message)
