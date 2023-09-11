from typing import List


def validate_battlefield(field: list):
    """
    This function is validating battleships field

    :param field:
    :return boolean value:
    """

    ship_length = {4: "single", 3: "cruiser", 2: "destroyer", 1: "submarine"}
    requirement_ships = {"submarine": 4, "destroyer": 3, "cruiser": 2, "single": 1}
    added_coordinates = set()
    row_size = len(field[0])
    column_size = len(field)
    is_1 = lambda x: x == "1"

    def ships_amount_check(ship_coords: list) -> bool:
        """
        this function is define type of ship,delete this ship from dict
        named "requirement_ships" and checks,if there more ships,than needed
        :param ship_coords:
        :return bull value:
        """
        if len(ship_coords) > 4:
            return False
        ship = ship_length[len(ship_coords)]
        if ship not in requirement_ships:
            return False
        requirement_ships[ship] -= 1
        if requirement_ships[ship] == 0:
            requirement_ships.pop(ship)
        return True

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
            if is_1(field[x][y]) and (x, y) not in added_coordinates:
                ship_coordinates = setting_ship_coords(x, y, row_size, column_size, field)
                if is_other_ship_around(ship_coordinates, row_size, column_size, field):
                    return False
                if not ships_amount_check(ship_coordinates):
                    return False
    return True
