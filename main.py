from data_structures import Window, Maze
import random as rd
def main():
    win = Window(800, 600)
    #maze = Maze(0, 0, 24, 32, 25, 25, win, rd.randrange(0, 10000))
    #maze = Maze(0, 0, 12, 16, 50, 50, win, rd.randrange(0, 10000))
    maze = Maze(0, 0, 6, 8, 100, 100, win, rd.randrange(0, 10000))
    maze._break_walls(0, 0)
    maze._reset_visited()
    if maze.solve():
        print("done")
    else:
        print("fail")
    win.wait_for_close()

if __name__ == "__main__":
    main()
