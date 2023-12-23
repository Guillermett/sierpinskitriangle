#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 23:36:21 2023

Sierpinski Triangle Project

@author: guillem
"""

import tkinter as tk
import math as math
import random
import time
import threading

# Draw Triangle

sin60 = math.sin(math.radians(60))

# Coords:
    
x0, y0 = 100, (100 + (sin60 * 400))
x1, y1 = 500, y0
x2, y2 = 300, 100

# Delay
delay = 0.0001
            
# Sierpinski drawer

def Sierpinski(iterations):
      
    # Choose the zone:
    z = random.randint(0, 2)
    
    # Limits to use:
    tan60 = math.tan(math.radians(60))
    m1 = 100 + (sin60 * 200)

    # Placing the first dot:
    if(z == 0 or z == 2):
        y = 100 + random.randint((math.ceil(sin60 * 200)), 
                           (math.floor(sin60 * 400)))
        h = y - m1
        r = h/tan60
        if(z == 0):
            x = random.randint((math.ceil(200 - r)),(math.floor(200 + r)))
        else:
            x = random.randint((math.ceil(400 - r)),(math.floor(400 + r)))
    elif(z == 1):
        y = m1 + random.randint(101, ((math.floor(sin60 * 200))))
        h = y - 100
        r = h/tan60
        x = random.randint((math.ceil(300 - r)),
                               (math.floor(300 + r)))

    canvas.create_oval(x, y, x, y, width = 1, fill = 'red')
    
    # Place the rest of the dots
    for i in range(iterations): 
        if stopped:
            break

        time.sleep(delay)             
        z1 = random.randint(0,2)
        
        if(z1 == 0 or z1 == 2):
            ym = ((y - y0)/2) + y0
            if(z1 == 0):
                xm = ((x - x0)/2) + x0
            else:
                xm = ((x - x1)/2) + x1
        else:
            ym = ((y - y2)/2) + y2
            xm = ((x - x2)/2) + x2
            
        y = ym
        x = xm

        canvas.create_oval(xm, ym, xm, ym, width = 1, fill = 'black')
        window.update()

def start():
    with lock: 
        global stopped
        stopped = False
    
def end():
    with lock:
        global stopped
        stopped = True
    

def get_input():
        
    try:
        iterations = int(entry.get())
        start()
        if (iterations > 0 and stopped == False):
                # Call the Sierpinski function with the specified iterations
                thread = threading.Thread(target = Sierpinski, 
                                          args = (iterations,))
                thread.start()
        else:
            print("Please input a positive number")
    except ValueError:
        print("Please input an integer")
        
def clear_canvas():
    end()
    canvas.delete('all')
    canvas.create_polygon(x0, y0, x1, y1, x2, y2, outline = 'black', 
                          fill = 'white')
    print(stopped)

# Create the main windoxxssw
window = tk.Tk()

# Set the window title
window.title("Sierpinski Triangle")

# Set the window size
window.geometry("800x600")  

canvas = tk.Canvas(window, width = 600, height = 500)
canvas.pack()

canvas.create_polygon(x0, y0, x1, y1, x2, y2, outline = 'black', 
                      fill = 'white')
# Entry widget
entry = tk.Entry(window)
entry.pack()

# Button to trigger the get_input function
Sierpinski_button = tk.Button(window, text = 'Run it', command = get_input)
Sierpinski_button.pack()

Reset_button = tk.Button(window, text = 'Reset Canvas', command = clear_canvas)
Reset_button.pack()

# Global vars
stopped = False
lock = threading.Lock()
                                                     
# Run it
window.mainloop()

