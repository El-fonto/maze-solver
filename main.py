from draw_graphics import Point, Window, Line


def main():
    win = Window(800, 600)
    line_1 = Line(Point(50, 50), Point(200, 200))
    line_2 = Line(Point(250, 25), Point(500, 570))
    win.draw_line(line_1, "black")
    win.draw_line(line_2, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
