from string import ascii_uppercase
from random import choice
from json import dumps

Cell = dict[str, int]
Part = dict[Cell, bool]
Coordinates = list[Part]

# the base Battleship class


class Battleship:
  count = 0
  fleet = {
      "carrier": {
          "length": 5
      },
      "battleship": {
          "length": 4
      },
      "destroyer": {
          "length": 3
      },
      "submarine": {
          "length": 3
      },
      "patrol_boat": {
          "length": 2
      }
  }
  columns: list[int] = []
  columns.extend(range(1, 11))
  rows = list(ascii_uppercase[:10])
  cells_taken: list[Cell] = []

  def __init__(self, type: str):
    self.type = type
    self.length = Battleship.fleet.get(type).get("length")
    Battleship.count += 1
    self.ship_id = Battleship.count
    self.init_coordinates()
    self.alive = True

  def set_coordinate(self, row: str, column: int):
    new_cell: Cell = {
        "row": row,
        "column": column
    }
    Battleship.cells_taken.append(new_cell)
    new_part: Part = {
        "cell": new_cell,
        "hit": False
    }
    self.coordinates.append(new_part)

  def populate_horizontal(self, start_row, start_column, count):
    column_pointer = Battleship.columns.index(start_column)
    for i in range(0, count):
      if i == 0:
        self.set_coordinate(start_row, Battleship.columns[column_pointer])
        return
      if {"row": start_row, "column": Battleship.columns[column_pointer]} in Battleship.cells_taken:
        self.init_coordinates()
        return
      self.set_coordinate(start_row, Battleship.columns[column_pointer])
      column_pointer += 1

  def populate_vertical(self, start_row, start_column, count):
    row_pointer = Battleship.rows.index(start_row)
    for i in range(0, count):
      if i == 0:
        self.set_coordinate(Battleship.rows[row_pointer], start_column)
        return
      if {"row": Battleship.rows[row_pointer], "column": start_column} in Battleship.cells_taken:
        self.init_coordinates()
        return
      self.set_coordinate(Battleship.rows[row_pointer], start_column)
      row_pointer += 1

  def init_coordinates(self):
    self.coordinates: Coordinates = []
    start_row = choice(Battleship.rows)
    start_column = choice(Battleship.columns)
    rand_direction = choice(["horizontal", "vertical"])
    count = self.length
    if rand_direction == "horizontal":
      self.populate_horizontal(start_row, start_column, count)
      return
    if rand_direction == "vertical":
      self.populate_vertical(start_row, start_column, count)
      return

  def hit(self, row: str, column: int):
    hit_cells = 0
    for i in range(0, len(self.coordinates)):
      if self.coordinates[i]["hit"] == True:
        hit_cells += 1
      if self.coordinates[i]["cell"]["row"] == row and self.coordinates[i]["column"] == column:
        print(f'HIT at {row}{column}!')
        self.coordinates[i]["hit"] = True
        return
    if hit_cells == len(self.coordinates):
      self.alive = False
      print("Ship is dead!")
      return
    print("No hit!")
    
