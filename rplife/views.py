import curses
from time import sleep
from rplife.grid import LifeGrid
__all__ = ["CursesView", "TKInterView"]



class CursesView:
    def __init__(self, pattern, alivesymbol, gen=10, frame_rate=7, bbox=(0, 0, 20, 20)):
        self.pattern = pattern
        self.alivesymbol= alivesymbol
        self.gen = gen
        self.frame_rate = frame_rate
        self.bbox = bbox
        
        
    def show(self):
        curses.wrapper(self._draw)

    def _draw(self, screen):
        current_grid = LifeGrid(self.pattern, self.alivesymbol)
        curses.curs_set(0)
        screen.clear()

        try:
            screen.addstr(0, 0, current_grid.as_string(self.bbox))
        except curses.error:
            raise ValueError(
                f"Error: terminal too small for pattern '{self.pattern.name}'"
            )

        for _ in range(self.gen):
            current_grid.evolve()
            screen.addstr(0, 0, current_grid.as_string(self.bbox))
            screen.refresh()
            sleep(1 / self.frame_rate)

from tkinter import Tk, Label, Canvas

class TKInterView:
    def __init__(self, pattern, alivesymbol, gen=10, frame_rate=7, bbox=(0, 0, 20, 20)):
        self.pattern = pattern
        self.alivesymbol= alivesymbol
        self.gen = gen
        self.frame_rate = frame_rate
        self.bbox = bbox

    def show(self):
        cell_size = 20
        root = Tk()
        root.title("Benjamins Game of Life")
        label = Label(root, text=self.pattern.name)
        label.pack()

        start_col, start_row, end_col, end_row = self.bbox
        row_count = end_row - start_row
        col_count = end_col - start_col
        canvas = Canvas(root, bg="white", width=col_count * cell_size, height=row_count * cell_size)
        canvas.pack()
        
        current_grid = LifeGrid(self.pattern, self.alivesymbol)
        for _ in range(self.gen):
            current_grid.evolve()

            canvas.delete("all")
            rows = current_grid.as_array(self.bbox)

            for y, row in enumerate(rows):
                for x, alive in enumerate(row):
                    if alive:
                        canvas.create_rectangle(x*cell_size, y*cell_size,(x+1)*cell_size,(y+1)*cell_size,fill="black")

            root.update()
            sleep(1 / self.frame_rate)
        root.mainloop()