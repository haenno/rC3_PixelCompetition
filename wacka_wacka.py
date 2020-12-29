# Pacmac runs random over the screen... *wacka! wacka!
# for PixelCompetition on rC3 (remote Chaos Communication Congress)
# Stream https://www.youtube.com/user/jschlingensiepen/live 
# Author: Henning 'haenno' Beier, haenno@web.de (2020)
# License: The Unlicense, https://unlicense.org

from time import sleep,time
import threading
import requests
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

def run_pacman(row):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(3.0)
        result = sock.connect_ex(('box.pixel-competition.de', 2342))
        if result == 0:
            for running_x_axis in range (0, 1920, +65):
                for i in range(0, img.size[0]):
                    for j in range(0, img.size[1]):
                        intsum = int(arr[j][i][0]) + int(arr[j][i][1]) + int(arr[j][i][2])  
                        if intsum < 765:
                            cmd = ('PX %d %d %d %d %d\n' % ((i + running_x_axis),(j + row),arr[j][i][0],arr[j][i][1],arr[j][i][2]))
                            sock.send(cmd.encode())
        sock.close()
    except Exception as error_message:
        handle_error(error_message)

def wacka_wacka():
    loop_timeout = time() + 25
    write_to_console("Letting Pacman lose...")
    for row in random.sample(range(1, 1080), 5): 
        threading.Thread(target=run_pacman, args=[int(row)]).start()
        write_to_console("  ..>> Eating row " + str(row))        
        sleep(2.5)
    while threading.active_count() != 1: 
        write_to_console(" > Remaing Rows to eat: "+ str(threading.active_count()-1))
        sleep(1.5)        
        if time() > loop_timeout:
            write_to_console("...Timelimit hit, starting next pacman.")
            return "timeout"
    write_to_console("...done.")
    return "ok"

img = Image.open('wacka_wacka_pm.bmp')
img = img.convert('RGBA')
arr = np.array(img)

while True:
    try:
        wacka_wacka()
    except Exception as error_message:
        handle_error(error_message)
