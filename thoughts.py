import time
import random
from tkinter import *

class ThoughtBox:
    def __init__(self, canvas:Canvas):
        self._canvas:Canvas = canvas
        self._lastToggleCursor = time.time()
        self._flagShowCursor = True
        self._blinkInterval = 0.5

        self.text = "Hello World!"
        self.rectangle = self._canvas.create_rectangle(10, 250, 515, 350, outline="white", width=5)
        self.textbox = self._canvas.create_text(30,300,fill="white", font="Times 20 italic bold", text=self.text, anchor=SW)
        
    def blink(self):
        if time.time() > self._lastToggleCursor+self._blinkInterval:
            self._flagShowCursor = not self._flagShowCursor
            self._lastToggleCursor = time.time()
        if self._flagShowCursor:
            self._canvas.itemconfig(self.textbox, text=self.text+'_')
        else:
            self._canvas.itemconfig(self.textbox, text=self.text)
    
    def getNewThought(self, filename):
        with open(filename) as fileStream:
            lines=fileStream.read().splitlines()
            self.text = random.choice(lines)
        self._canvas.itemconfig(self.textbox, state='normal')
        self._canvas.itemconfig(self.rectangle, state='normal')

    def hideThoughtBox(self):
        self._canvas.itemconfig(self.textbox, state='hidden')
        self._canvas.itemconfig(self.rectangle, state='hidden')