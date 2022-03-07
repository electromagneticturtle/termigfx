import time
import sys
import os


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def center(msg):
    msg_buffr = ""
    width, height = os.get_terminal_size()
    t_width, t_height = len(msg), (list(msg).count("\n") + 2)
    for n in range(height//2 - t_height//2):
        msg_buffr += "\n"
    for m in range(width//2 - t_width//2):
        msg_buffr += " "
    msg_buffr += msg
    for m in range(width//2 - t_width//2):
        msg_buffr += " "
    for n in range(height//2 - t_height//2 - 1):
        msg_buffr += "\n"
    return msg_buffr


def typewrite(msg, emptychar=False):
    list_msg = list(msg)
    for char in list_msg:
        sys.stdout.write(char)
        if not emptychar and (char != " " and char != "\n"):
            sys.stdout.flush()
            time.sleep(0.05)


def overlay(front, back):
    
    raster = ""
    
    max_height = max(len(front.split("\n")), len(back.split("\n")))
    for h in range(max_height):
        if (len(front.split("\n")) - 1) >= h and (len(back.split("\n")) - 1) >= h:
            max_width = max(len(front.split("\n")[h]), len(back.split("\n")[h]))
            for w in range(max_width):
                if (len(front.split("\n")[h]) - 1) >= w and (len(back.split("\n")[h]) - 1) >= w:
                    if front.split("\n")[h][w] == " " and back.split("\n")[h][w] != "":
                        raster += back.split("\n")[h][w]
                    else:
                        raster += front.split("\n")[h][w]
                elif (len(front.split("\n")[h]) - 1) < w:
                    raster += back.split("\n")[h][w]
                elif (len(back.split("\n")[h]) - 1) < w:
                    raster += front.split("\n")[h][w]
            if h < (max_height - 1):
                raster += "\n"
        elif (len(front.split("\n")) - 1) < h:
            raster += back.split("\n")[h]
            if h < (max_height - 1):
                raster += "\n"
        elif (len(back.split("\n")) - 1) < h:
            raster += front.split("\n")[h] 
            if h < (max_height - 1):
                raster += "\n"
            
    return raster
            