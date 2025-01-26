from data_structures import Line, Point, Window
def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(40, 50), Point(460, 380)), "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()