import collections

ALIVE = "♥" # variabel for hvilket symbol som brukes for levende celler (deafult)
DEAD = "‧" # variabel for hvilken symbol som brukes for døde celler

class LifeGrid:
    def __init__(self, pattern, alivesymbol):
        self.pattern = pattern
        self.alivesymbol= alivesymbol

    def evolve(self): # denne koden er for å hvise hvilket kordinater celler skal leve eller død etter en evulosjon
        neighbors = (
            (-1, -1),  # Above left
            (-1, 0),  # Above
            (-1, 1),  # Above right
            (0, -1),  # Left
            (0, 1),  # Right
            (1, -1),  # Below left
            (1, 0),  # Below
            (1, 1),  # Below right
        )
        num_neighbors = collections.defaultdict(int)
        for row, col in self.pattern.alive_cells:
            for drow, dcol in neighbors:
                num_neighbors[(row + drow, col + dcol)] += 1

        stay_alive = { # Finn cellene som vil forbli i live ved å identifisere naboer som har to eller tre levende naboer selv, og deretter finne de felles cellene med de allerede levende cellene.
            cell for cell, num in num_neighbors.items() if num in {2, 3}
        } & self.pattern.alive_cells
        come_alive = {
            cell for cell, num in num_neighbors.items() if num == 3
        } - self.pattern.alive_cells

        self.pattern.alive_cells = stay_alive | come_alive

    def as_string(self, bbox):
        start_col, start_row, end_col, end_row = bbox
        display = [self.pattern.name.center(2 * (end_col - start_col))]
        for row in range(start_row, end_row):
            display_row = [
                self.alivesymbol if (row, col) in self.pattern.alive_cells else DEAD
                for col in range(start_col, end_col)
            ]
            display.append(" ".join(display_row))
        return "\n ".join(display)

    def __str__(self):
        return (
            f"{self.pattern.name}:\n"
            f"Alive cells -> {sorted(self.pattern.alive_cells)}"
        )


    


