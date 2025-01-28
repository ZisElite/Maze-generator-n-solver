from typing import *
from tkinter import Tk, BOTH, Canvas
import time
import random as rd

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
        #print(self)
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
    def __init__(self, x1, y1, x2, y2, win:Window=None):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self._visited = False
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
    
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
            self._win.draw_line(top_line, "black")
        else:
            self._win.draw_line(top_line, "white")
        if self.has_bottom_wall:
            self._win.draw_line(bot_line, "black")
        else:
            self._win.draw_line(bot_line, "white")
        if self.has_left_wall:
            self._win.draw_line(left_line, "black")
        else:
            self._win.draw_line(left_line, "white")
        if self.has_right_wall:
            self._win.draw_line(right_line, "black")
        else:
            self._win.draw_line(right_line, "white")
        
    def draw_move(self, to_cell:Self, undo=False):
        center1 = Point((self._x1 + self._x2)//2, (self._y1 + self._y2)//2)
        center2 = Point((to_cell._x1 + to_cell._x2)//2, (to_cell._y1 + to_cell._y2)//2)
        color = "gray" if undo else "red"
        self._win.draw_line(Line(center1, center2), color)

class Maze:
    def __init__(self, x:int, y:int, rows:int, columns:int, cell_size_x:int, cell_size_y:int, win:Window=None, seed:int=0):
        self.x = x
        self.y = y
        self.rows = rows
        self.columns = columns
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        rd.seed(seed)
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.columns):
            self._cells.append([])
            for j in range(self.rows):
                self._cells[-1].append(Cell(self.x + i*self.cell_size_x, self.y + j*self.cell_size_y, self.x + (i+1)*self.cell_size_x, self.y + (j+1)*self.cell_size_y, self.win))
        self._create_entrance_and_exit()
        if self.win:
            for i in range(self.columns):
                for j in range(self.rows):
                    self._draw_cell(i, j)

    def _draw_cell(self, x, y):
        self._cells[x][y].draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
    
    def _create_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[-1][-1].has_right_wall = False
    
    def _break_walls(self, x, y):
        self._cells[x][y]._visited = True
        while True:
            adjacent = []
            if 0 <= x-1 < self.columns and 0 <= y < self.rows and not self._cells[x-1][y]._visited:
                adjacent.append("left")
            if 0 <= x < self.columns and 0 <= y-1 < self.rows and not self._cells[x][y-1]._visited:
                adjacent.append("top")
            if 0 <= x+1 < self.columns and 0 <= y < self.rows and not self._cells[x+1][y]._visited:
                adjacent.append("right")
            if 0 <= x < self.columns and 0 <= y+1 < self.rows and not self._cells[x][y+1]._visited:
                adjacent.append("bottom")
            if not adjacent:
                self._draw_cell(x, y)
                return
            wall = adjacent[rd.randrange(0, len(adjacent))]
            if wall == "left":
                self._cells[x][y].has_left_wall = False
                self._cells[x-1][y].has_right_wall = False
                self._draw_cell(x, y)
                self._draw_cell(x-1, y)
                self._cells[x][y].draw_move(self._cells[x-1][y])
                next = [x-1, y]
            elif wall == "right":
                self._cells[x][y].has_right_wall = False
                self._cells[x+1][y].has_left_wall = False
                self._draw_cell(x, y)
                self._draw_cell(x+1, y)
                self._cells[x][y].draw_move(self._cells[x+1][y])
                next = [x+1, y]
            elif wall == "top":
                self._cells[x][y].has_top_wall = False
                self._cells[x][y-1].has_bottom_wall = False
                self._draw_cell(x, y)
                self._draw_cell(x, y-1)
                self._cells[x][y].draw_move(self._cells[x][y-1])
                next = [x, y-1]
            else:
                self._cells[x][y].has_bottom_wall = False
                self._cells[x][y+1].has_top_wall = False
                self._draw_cell(x, y)
                self._draw_cell(x, y+1)
                self._cells[x][y].draw_move(self._cells[x][y+1])
                next = [x, y+1]
            self._break_walls(next[0], next[1])
    
    def _reset_visited(self):
        for i in range(self.columns):
            for j in range(self.rows):
                self._cells[i][j]._visited = False