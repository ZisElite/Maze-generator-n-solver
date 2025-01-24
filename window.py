from tkinter import Tk, BOTH, Canvas

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