from graphics import Point, Line, Window


class Cell:
    def __init__(
        self,
        window: Window | None = None,
    ) -> None:
        self._win = window

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1: int | None = None
        self._x2: int | None = None
        self._y1: int | None = None
        self._y2: int | None = None

        self.visited = False

    def draw(self, x1: int, y1: int, x2: int, y2: int) -> None:
        if self._win is None:
            return

        # values updated to use later
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        # corners
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)

        # when walls are false, they're white
        if self.has_left_wall:
            left_wall = Line(top_left, bottom_left)
            self._win.draw_line(left_wall)
        else:
            left_wall = Line(top_left, bottom_left)
            self._win.draw_line(left_wall, "white")

        if self.has_top_wall:
            top_wall = Line(top_left, top_right)
            self._win.draw_line(top_wall)
        else:
            top_wall = Line(top_left, top_right)
            self._win.draw_line(top_wall, "white")

        if self.has_right_wall:
            right_wall = Line(top_right, bottom_right)
            self._win.draw_line(right_wall)
        else:
            right_wall = Line(top_right, bottom_right)
            self._win.draw_line(right_wall, "white")

        if self.has_bottom_wall:
            bottom_wall = Line(bottom_left, bottom_right)
            self._win.draw_line(bottom_wall)
        else:
            bottom_wall = Line(bottom_left, bottom_right)
            self._win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo: bool = False) -> None:
        if self._win is None:
            return

        self_center = Point(((self._x1 + self._x2) // 2), ((self._y1 + self._y2) // 2))

        to_cell_center = Point(
            ((to_cell._x1 + to_cell._x2) / 2), ((to_cell._y1 + to_cell._y2) / 2)
        )

        line = Line(self_center, to_cell_center)

        if not undo:
            self._win.draw_line(line, fill_color="green")
        else:
            self._win.draw_line(line, fill_color="red")

    def draw_from_center(
        self, center_x: int, center_y: int, cell_size_x: int, cell_size_y: int
    ):
        """
        Calculate all coordinates from center point and dimensions
        """
        x1 = center_x - (cell_size_x // 2)
        y1 = center_y - (cell_size_y // 2)
        x2 = center_x + (cell_size_x // 2)
        y2 = center_y + (cell_size_y // 2)

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self.draw(x1, y1, x2, y2)
