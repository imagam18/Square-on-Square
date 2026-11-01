import math


def get_rotated_square(cx, cy, angle, size=1):

    half = size / 2

    corners = [
        (-half, -half),
        (half, -half),
        (half, half),
        (-half, half)
    ]

    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    rotated_corners = []

    for x, y in corners:

        new_x = x * cos_a - y * sin_a
        new_y = x * sin_a + y * cos_a

        final_x = cx + new_x
        final_y = cy + new_y

        rotated_corners.append((final_x, final_y))

    return rotated_corners