from typing import *
from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start:Point, end:Point):
        self.start = start
        self.end = end
    
    def draw(self, canvas:Canvas, fill_color:str):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)

class Window:
    def __init__(self, width, height):
        self.app = Tk()
        self.app.title = "Mazed"
        self.app.minsize(width, height)
        self.app.maxsize(width, height)
        self.canvas = Canvas(self.app)
        self.canvas.pack()
        self.running = False
        self.app.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.app.update_idletasks()
        self.app.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
    
    def draw_line(self, line:Line, fill_color:str):
        line.draw(self.canvas, fill_color)