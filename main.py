from graphics import Window
from maze import Maze


def main():
    num_rows = 12
    num_cols = 16
    scr_margin = 50
    screen_width = 800
    screen_height = 600
    cell_size_x = (screen_width - 2 * scr_margin) // num_cols
    cell_size_y = (screen_height - 2 * scr_margin) // num_rows
    win = Window(screen_width, screen_height)
    seed = 10

    maze = Maze(
        scr_margin, scr_margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed
    )

    win.wait_for_close()


if __name__ == "__main__":
    main()
