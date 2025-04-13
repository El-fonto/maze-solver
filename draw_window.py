from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title()
        self.canvas = Canvas()
