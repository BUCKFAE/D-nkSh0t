from typing import Tuple


def coordinates_to_width_height(coord1: Tuple[int, int], coord2: Tuple[int, int]) -> Tuple[int, int]:
    return coord2[0] - coord1[0], coord2[1] - coord1[1]


def is_same_color(image, pos_x, pos_y, color) -> bool:
    return all([image[pos_y][pos_x][i] == color[i] for i in range(3)])
