from graphics import Point, Line, Window


class Cell:
    def __init__(
        self,
        window: Window,
    ) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._win = window

        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

    def draw(self, x1, y1, x2, y2) -> None:
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Coordinates must satisfy x1 < x2 and y1 < y2.")

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)

        if self.has_left_wall:
            left_wall = Line(top_left, bottom_left)
            self._win.draw_line(left_wall)

        if self.has_top_wall:
            top_wall = Line(top_left, top_right)
            self._win.draw_line(top_wall)

        if self.has_right_wall:
            right_wall = Line(top_right, bottom_right)
            self._win.draw_line(right_wall)

        if self.has_bottom_wall:
            bottom_wall = Line(bottom_left, bottom_right)
            self._win.draw_line(bottom_wall)
