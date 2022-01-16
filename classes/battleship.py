from string import ascii_uppercase
from random import randint

Cell = dict["row": str, "column": int]
Part = dict["cell": Cell, "hit": bool]
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
  rows: list[int] = []
  rows.extend(range(1, 11))
  columns = list(ascii_uppercase[:10])

  def __init__(self, type: str):
    self.type = type
    self.length = Battleship.fleet.get(type).get("length")
    Battleship.count += 1
    self.ship_id = Battleship.count
    self.coordinates = []
    self.init_coordinates()
    self.alive = True

  def set_coordinate(self, row: str, column: str):
    new_cell = {
      "cell": {
        "row": row,
        "column": column
      },
      "hit": False
    }
    if new_cell in self.coordinates: return
    self.coordinates.append(new_cell)

  def init_coordinates(self):
    p_1 = randint(0, 9)
    p_2 = randint(0, 9)
    count = self.length
    while count > 0 and not Battleship.rows[p_1] and not Battleship.columns[p_2]:
      p_1 = randint(0, 9)
      p_2 = randint(0, 9)
      rand_row = Battleship.rows.pop(p_1)
      rand_column = Battleship.columns.pop(p_2)
      self.set_coordinate(rand_row, rand_column)

  def hit(self, cell: Cell):
    for i in range(0, len(self.coordinates)):
      if self.coordinates[i]["cell"]["row"] == cell["row"] and self.coordinates[i]["column"] == cell["column"]:
        print(f'HIT at {cell["row"]}{cell["column"]}!')
        self.coordinates[i]["hit"] = True
