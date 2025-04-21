import time
from graphics import Window
from cell import Cell


class Maze:
    def __init__(
        self,
        x1: int,  # initial position of the maze
        y1: int,  # initial position of the maze
        num_rows: int,
        num_cols: int,
        cell_size_x: int,  # determine cell size
        cell_size_y: int,  # determine cell size
        win: Window | None = None,
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._cells: list[list[Cell]] = []  # list matrix

        self._create_cells()

    def _create_cells(self):
        """Populate a two level list and draw cells"""
        for i in range(self._num_cols):
            column: list[Cell] = []
            for j in range(self._num_rows):
                c = Cell(self._win)
                column.append(c)
            self._cells.append(column)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        """calculate position and draw from draw the cell"""
        if self._win is None:
            return
        c = self._cells[i][j]

        cell_x = self._x1 + i * self._cell_size_x
        cell_y = self._y1 + j * self._cell_size_y

        c.draw_from_center(cell_x, cell_y, self._cell_size_x, self._cell_size_y)

        self._animate()

    def _animate(self):
        """visualize the algoritm"""
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
