import time
import random
from graphics import Window
from cell import Cell


class Maze:
    def __init__(
        self,
        x1: int,  # initial position of the maze
        y1: int,  # initial position of the maze
        num_cols: int,
        num_rows: int,
        cell_size_x: int,  # determine cell size
        cell_size_y: int,  # determine cell size
        win: Window | None = None,
        seed: int | None = None,
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_cols = num_cols
        self._num_rows = num_rows
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed:
            random.seed(seed)

        self._cells: list[list[Cell]] = []  # list matrix

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def solve(self) -> bool:
        """initializes depth first search to solve the maze"""
        return self._solve_r(i=0, j=0)

    def _solve_r(self, i: int, j: int) -> bool:
        """checks if cell is the last cell if not: check which cells are not visited, go there; recurse"""
        self._animate()

        c = self._cells[i][j]
        c.visited = True

        # end goal // [num_cols-1][num_rows-1] is the last cell
        if c == self._cells[self._num_cols - 1][self._num_rows - 1]:
            return True

        poss_directions: list[tuple[Cell, int, int]] = []

        # up [i: current row][j-1: row above]
        if (
            j > 0
            and not self._cells[i][j - 1].has_bottom_wall
            and not self._cells[i][j - 1].visited
        ):
            poss_directions.append((self._cells[i][j - 1], i, j - 1))
        # left
        if (
            i > 0
            and not self._cells[i - 1][j].has_right_wall
            and not self._cells[i - 1][j].visited
        ):
            poss_directions.append((self._cells[i - 1][j], i - 1, j))
        # right
        if (
            i < self._num_cols - 1
            and not self._cells[i + 1][j].has_left_wall
            and not self._cells[i + 1][j].visited
        ):
            poss_directions.append((self._cells[i + 1][j], i + 1, j))
        # down
        if (
            j < self._num_rows - 1
            and not self._cells[i][j + 1].has_top_wall
            and not self._cells[i][j + 1].visited
        ):
            poss_directions.append((self._cells[i][j + 1], i, j + 1))

        for moving_cell in poss_directions:
            c.draw_move(moving_cell[0])
            if self._solve_r(i=moving_cell[1], j=moving_cell[2]):
                return True
            else:
                c.draw_move(to_cell=moving_cell[0], undo=True)
        return False

    def _reset_cells_visited(self):
        """removes visited data from cells to draw them later"""
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _break_walls_r(self, i: int, j: int):
        """draws broken walls in a random direction"""
        c = self._cells[i][j]

        c.visited = True

        while True:
            poss_directions: list[tuple[int, int, str]] = []

            # up [i: current row][j-1: row above]
            if j > 0 and not self._cells[i][j - 1].visited:
                poss_directions.append((i, j - 1, "up"))
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                poss_directions.append((i - 1, j, "left"))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                poss_directions.append((i + 1, j, "right"))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                poss_directions.append((i, j + 1, "down"))

            if len(poss_directions) == 0:
                self._draw_cell(i, j)
                return

            # pick random direction from the list
            rand_direction = random.randrange(len(poss_directions))
            chosen_direction = poss_directions[rand_direction][2]

            if chosen_direction == "up":
                # current wall
                self._cells[i][j].has_top_wall = False
                # relative up-cell
                self._cells[i][j - 1].has_bottom_wall = False
                self._break_walls_r(i, j - 1)

            if chosen_direction == "left":
                # current wall
                self._cells[i][j].has_left_wall = False
                # relative left-cell
                self._cells[i - 1][j].has_right_wall = False
                self._break_walls_r(i - 1, j)

            if chosen_direction == "right":
                # current wall
                self._cells[i][j].has_right_wall = False
                # relative right-cell
                self._cells[i + 1][j].has_left_wall = False
                self._break_walls_r(i + 1, j)

            if chosen_direction == "down":
                # current wall
                self._cells[i][j].has_bottom_wall = False
                # relative down-cell
                self._cells[i][j + 1].has_top_wall = False
                self._break_walls_r(i, j + 1)

    def _break_entrance_and_exit(self):
        """First cell doesn't have top wall and last cell doesn't have bottom"""
        last_cell_col = self._num_cols - 1
        last_cell_row = self._num_rows - 1

        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[last_cell_col][last_cell_row]

        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)

        exit_cell.has_bottom_wall = False
        self._draw_cell(last_cell_col, last_cell_row)

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

    def _draw_cell(self, i: int, j: int):
        """calculate position and draw from draw the cell"""
        if self._win is None:
            return
        c = self._cells[i][j]

        cell_x = self._x1 + i * self._cell_size_x
        cell_y = self._y1 + j * self._cell_size_y

        c.draw_from_center(cell_x, cell_y, self._cell_size_x, self._cell_size_y)

        self._animate()

    def _animate(self):
        """visualize the algorithm"""
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.005)
