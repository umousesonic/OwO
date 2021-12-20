import sounddevice as sd
import numpy as np
from tkinter import *

class Audio_Visualizer:
    def __init__(self, canvas):
        self._canvas:Canvas = canvas
        self._flagShow:bool = False

        self._x0 = 175
        self._x1 = 350
        self._y0 = 67
        self._y1 = 233

        self._barWidth = 10
        self._interval = 2

        pass

    def print_sound(self, indata, outdata, frames, time, status):
        volume_norm = np.linalg.norm(indata)*10
        print ("|" * int(volume_norm))

    def show(self):
        self._canvas.create_rectangle(self._x0, self._y0, self._x1, self._y1, outline="white", width=5)
        with sd.Stream(callback=self.print_sound):
            while self._flagShow:
                pass
    

