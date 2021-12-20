import tkinter
import time
import os
import random

from eyes import *
from thoughts import *

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

def enterFullScreen(event=None):
    window.attributes("-fullscreen", True)
    return "break"

def endFullScreen(event=None):
    window.attributes("-fullscreen", False)
    return "break"

window = tkinter.Tk()
window.title('animation test')
window.config(cursor="none")

window.bind("<F11>", enterFullScreen)
window.bind("<Escape>", endFullScreen)
window.attributes("-fullscreen", True)

canvas = tkinter.Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight(), bg="black", highlightthickness=0)
canvas.pack()

myeyes = Eyes(canvas, window)
lastEyeAtime = time.time()
blinkInterval:float = 0

myThoughts = ThoughtBox(canvas)
updateThoughtPossibility = 25.0
cycleInterval:float = 7
lastUpdateThoughtTime = time.time()

while 1:
    window.update()

    # blink eyes
    if time.time() > lastEyeAtime+blinkInterval:
        if myeyes.blink():
            lastEyeAtime = time.time()
            blinkInterval:float = ((3000+random.randint(-3000, 3000))/1000)
            
    
    # blink cursor
    myThoughts.blink()

    # update text
    if time.time() > lastUpdateThoughtTime+cycleInterval:
        randomNum = float(random.randint(0, 10000)/100)
        if randomNum < updateThoughtPossibility:
            myThoughts.getNewThought("/home/pi/Desktop/OwO/thoughts.txt")
        else:
            # hide thoughts if expired
            myThoughts.hideThoughtBox()
        lastUpdateThoughtTime = time.time()
        
    



window.mainloop()


