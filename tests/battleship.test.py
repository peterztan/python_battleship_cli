import unittest

from battleship import Battleship

ship_names = ["carrier", "battleship", "destroyer", "submarine", "patrol_boat"]
fleet: list[Battleship] = []
for name in ship_names:
  ship = Battleship(name)
  fleet.append(ship)

class TestBattleship(unittest.TestCase):
  
  def test_ship_type(self):
    pass