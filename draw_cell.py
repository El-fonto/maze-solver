from draw_graphics import Point, Line, Window


class Cell:
    def __init__(
        self,
        p1: Point,
        p2: Point,
        has_left_wall: bool = True,
        has_right_wall: bool = True,
        has_top_wall: bool = True,
        has_bottom_wall: bool = True,
        window=None,
    ) -> None:
        """
        Each cell can be modified on each individual instance
        """
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = p1.x
        self._x2 = p2.x
        self._y1 = p1.y
        self._y2 = p2.y
        self._win = None


#!TODO:
# Draw method for cell class with coordinates
# assign window that goes in the constructor
# update main.py
