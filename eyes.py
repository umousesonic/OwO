import time
from tkinter import *

class Eyes:
    def __init__(self, canvas, window):
        self._canvas:Canvas = canvas
        self._window:Tk = window
        self.eyes = []
        self.eyes.append(self._canvas.create_oval(101, 67, 136, 167, fill="white"))
        self.eyes.append(self._canvas.create_oval(363, 67, 398, 167, fill="white"))

        self.lids = []
        self.startY = 67
        self.endY = 167
        self.lids.append(self._canvas.create_rectangle(101, 67, 136, self.startY, fill="black"))
        self.lids.append(self._canvas.create_rectangle(363, 67, 398, self.startY, fill="black"))

        self._blinkState = 0
        self._lidY = 67
        pass

    def drawEyes(self):
        eyes = []
        eyes.append(self._canvas.create_oval(101, 67, 136, 167, fill="white"))
        eyes.append(self._canvas.create_oval(363, 67, 398, 167, fill="white"))
        return eyes

    def blink(self):
        if self._blinkState == 0:
            self._lidY += 1
            self._canvas.coords(self.lids[0], 101, 67, 136, self._lidY)
            self._canvas.coords(self.lids[1], 363, 67, 398, self._lidY)
            if self._lidY > self.endY:
                self._blinkState = 1
            return False
        
        if self._blinkState == 1:
            self._lidY -= 1
            self._canvas.coords(self.lids[0], 101, 67, 136, self._lidY)
            self._canvas.coords(self.lids[1], 363, 67, 398, self._lidY)
            if self._lidY < self.startY:
                self._blinkState = 2
            return False
        
        if self._blinkState == 2:
            self._lidY = 67
            self._blinkState = 0
            return True
        

    def show(self):
        self._canvas.itemconfigure(self.eyes[0], state='normal')
        self._canvas.itemconfigure(self.eyes[1], state='normal')
    
    def hide(self):
        self._canvas.itemconfigure(self.eyes[0], state='hidden')
        self._canvas.itemconfigure(self.eyes[1], state='hidden')