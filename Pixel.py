# this will show the pixel color where mouse is hovered
from pyautogui import position
from pyautogui import screenshot
from time import sleep
from sys import stdout

def print_no_newline(string):
    stdout.write("\r")
    stdout.write(string + '       ')
    stdout.flush()

try:
    while True:
        x,y = position() # This will get the x & y pos on screen
        pixelColor = screenshot().getpixel((x,y)) # this will get the rgb val
        string =  f'rgb{pixelColor}'
        print_no_newline(string)
        sleep(3)

except KeyboardInterrupt:
    print('')
    print('Exiting :..')
