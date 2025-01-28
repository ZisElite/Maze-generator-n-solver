from data_structures import Window, Maze
def main():
    win = Window(800, 600)
    maze = Maze(10, 10, 20, 24, 25, 25, win)
    maze._break_walls(0, 0)
    maze._reset_visited()
    win.wait_for_close()

if __name__ == "__main__":
    main()