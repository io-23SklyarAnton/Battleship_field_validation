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
    validation_message = "Your field has passed validation!!!"
    is_1 = lambda x: x == 1

    def ships_amount_check(ship_coords: list) -> bool:
        """
        this function is define type of ship,delete this ship from dict
        named "requirement_ships" and checks,if there more ships,than needed
        :param ship_coords:
        :return bull value:
        """

        nonlocal validation_message

        if len(ship_coords) > 4:
            validation_message = f"oops,your ship on {ship_coords} is too big"
            return False

        ship = ship_length[len(ship_coords)]
        if ship not in requirement_ships:
            validation_message = f"oops,there is too much ships {ship} type"
            return False

        requirement_ships[ship] -= 1
        if requirement_ships[ship] == 0:
            requirement_ships.pop(ship)
        return True

    def is_other_ship_around(ship_coords: List[tuple], field: list) -> bool:
        """searching if any ship is close to our"""
        for x, y in ship_coords:
            try:
                if is_1(field[x + 1][y - 1]):
                    return True
            except IndexError:
                if is_1(field[x - 1][y - 1]):
                    return True
                continue
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
                if is_other_ship_around(ship_coordinates, field):
                    validation_message = f"oops, there is other ship around {ship_coordinates} coords"
                    return False, validation_message
                if not ships_amount_check(ship_coordinates):
                    return False, validation_message
    return True, validation_message


battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(validate_battlefield(battleField))
