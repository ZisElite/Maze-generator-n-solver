from data_structures import Line, Point, Window, Cell
def main():
    win = Window(800, 600)
    cell1 = Cell(100, 100, 300, 300, win)
    cell2 = Cell(300, 100, 500, 300, win)
    cell1.draw()
    cell2.draw()
    cell1.draw_move(cell2)
    win.wait_for_close()

if __name__ == "__main__":
    main()