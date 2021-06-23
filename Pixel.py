# this will show the pixel color where mouse is hovered
from pyautogui import position
from pyautogui import screenshot
from time import sleep
from sys import stdout
import blessed



color_list = []


def print_block(color):
    term = blessed.Terminal()
    print(f'rgb{color}')
    print(f'{term.on_color_rgb(color[0],color[1],color[2])}             {term.normal}')
    print(f'{term.on_color_rgb(color[0],color[1],color[2])}             {term.normal}')
    print(f'{term.on_color_rgb(color[0],color[1],color[2])}             {term.normal}')
    print(f'{term.on_color_rgb(color[0],color[1],color[2])}             {term.normal}')
    print(f'{term.on_color_rgb(color[0],color[1],color[2])}             {term.normal}')


def print_no_newline(string):    
    if string in color_list:
        color_list.append(string)
        return

    color_list.append(string)
    print_block(string)

try:
    while True:
        x,y = position() # This will get the x & y pos on screen
        pixelColor = screenshot().getpixel((x,y)) # this will get the rgb val
        print_no_newline(pixelColor)
        sleep(3)

except KeyboardInterrupt:
    print('')
    print('Exiting :..')
