from typing import List


def validate_battlefield(field: list):
    """
    This function is validating battleships field

    :param field:
    :return boolean value:
    """

    requirement_ships = {"submarine": 4, "destroyer": 3, "cruiser": 2, "single": 1}
    ship_size_counter = 0
    added_coordinates = set()
    row_size = len(field[0])
    column_size = len(field)
    is_1 = lambda x: x == "1"

    def is_other_ship_around(ship_coords: list, row_size: int, column_size: int, field: list) -> bool:
        """searching if any ship is close to our"""

        return False

    def setting_ship_coords(x: int, y: int, row_size: int, column_size: int, field: list) -> List[tuple]:
        """
        this function is searching parts of ship
        :param x, y, row_size, column_size, field:
        :return list of ship coordinates:
        """
        ship_coords = [(x, y)]
        ship_is_vertical = True
        if x != row_size:
            while is_1(field[x + 1][y]):
                x += 1
                ship_coords.append((x, y))
                added_coordinates.add((x, y))
                ship_is_vertical = False
        if y != column_size and ship_is_vertical:
            while is_1(field[x][y + 1]):
                y += 1
                ship_coords.append((x, y))
                added_coordinates.add((x, y))
        return ship_coords

    for x in range(column_size):
        for y in range(row_size):
            pass
    return True
