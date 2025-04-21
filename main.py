from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    m = Maze(
        x1=50,
        y1=50,
        num_rows=5,
        num_cols=5,
        cell_size_x=20,
        cell_size_y=20,
        win=win,
    )
    print(f"Number of columns: {len(m._cells)}")  # Expecting 5
    print(
        f"Number of rows in each column: {[len(col) for col in m._cells]}"
    )  # Expecting [5, 5, 5, 5, 5]

    win.wait_for_close()


if __name__ == "__main__":
    main()
