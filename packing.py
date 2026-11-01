import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def get_rotated_square(cx, cy, angle_degrees, size=1):

    half = size / 2

    corners = [
        (-half, -half),
        (half, -half),
        (half, half),
        (-half, half)
    ]

    angle = math.radians(angle_degrees)

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


# Five squares ki information
squares = [
    {"x": 0, "y": 0, "angle": 0},
    {"x": 2, "y": 0, "angle": 30},
    {"x": 4, "y": 0, "angle": 45},
    {"x": 0, "y": 2, "angle": 60},
    {"x": 2, "y": 2, "angle": 90}
]



fig, ax = plt.subplots(figsize=(8, 8))


# Har square ko draw karo
for i, square in enumerate(squares):

    corners = get_rotated_square(
        square["x"],
        square["y"],
        square["angle"]
    )

    polygon = Polygon(
        corners,
        closed=True,
        fill=False,
        linewidth=2,
        label=f"Square {i + 1}"
    )

    ax.add_patch(polygon)

    # Square ka center show karo
    ax.plot(square["x"], square["y"], "ro")

    # Square ka number show karo
    ax.text(
        square["x"],
        square["y"],
        str(i + 1)
    )


ax.set_xlim(-2, 6)
ax.set_ylim(-2, 4)

ax.set_aspect("equal")
ax.grid(True)

ax.set_title("Multiple Rotated Squares")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

ax.legend()

plt.show()