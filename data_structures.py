from typing import *
from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point: x={self.x} y={self.y}"

class Line:
    def __init__(self, start:Point, end:Point):
        self.start = start
        self.end = end
    
    def draw(self, canvas:Canvas, fill_color:str):
        print(self)
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)
    
    def __repr__(self):
        return f"Line: start[{self.start}] end[{self.end}]"

class Window:
    def __init__(self, width, height):
        self.app = Tk()
        self.app.title = "Mazed"
        self.app.minsize(width, height)
        self.app.maxsize(width, height)
        self.canvas = Canvas(self.app, width=width, height=height)
        self.canvas
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

class Cell:
    def __init__(self, x1, y1, x2, y2, win:Window):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self. has_left_wall = True
        self. has_right_wall = True
        self. has_top_wall = True
        self. has_bottom_wall = True
    
    def draw(self):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bot_left = Point(self._x1, self._y2)
        bot_right = Point(self._x2, self._y2)
        top_line = Line(top_left, top_right)
        bot_line = Line(bot_left, bot_right)
        left_line = Line(top_left, bot_left)
        right_line = Line(top_right, bot_right)
        if self.has_top_wall:
            print("top")
            self._win.draw_line(top_line, "black")
        if self.has_bottom_wall:
            print("bot")
            self._win.draw_line(bot_line, "black")
        if self.has_left_wall:
            print("left")
            self._win.draw_line(left_line, "black")
        if self.has_right_wall:
            print("right")
            self._win.draw_line(right_line, "black")
        
    def draw_move(self, to_cell:Self, undo=False):
        center1 = Point((self._x1 + self._x2)//2, (self._y1 + self._y2)//2)
        center2 = Point((to_cell._x1 + to_cell._x2)//2, (to_cell._y1 + to_cell._y2)//2)
        color = "gray" if undo else "red"
        self._win.draw_line(Line(center1, center2), color)