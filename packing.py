
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


# Function to calculate square corners
def get_square_corner(x, y, size):
    half = size / 2

    corners = [
        (x - half, y - half),  # Bottom-left
        (x + half, y - half),  # Bottom-right
        (x + half, y + half),  # Top-right
        (x - half, y + half)   # Top-left
    ]

    return corners


# Function to rotate square
def rotate_square(corners, angle):

    rotated_corners = []

    # Convert degrees into radians
    angle = math.radians(angle)

    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    # Rotate all four corners
    for x, y in corners:

        new_x = x * cos_a - y * sin_a
        new_y = x * sin_a + y * cos_a

        rotated_corners.append((new_x, new_y))

    return rotated_corners


# Create a unit square
corners = get_square_corner(0, 0, 1)


# Rotate the square by 30 degrees
rotated_corners = rotate_square(corners, 30)


# Display original corners
print("Original square corners:")

for corner in corners:
    print(corner)


# Display rotated corners
print("\nRotated square corners:")

for corner in rotated_corners:
    print(corner)


# Create figure and axes
fig, ax = plt.subplots()


# Draw original square
square = Polygon(
    corners,
    closed=True,
    fill=False,
    edgecolor="blue",
    linewidth=2,
    label="Original Square"
)

ax.add_patch(square)


# Draw rotated square
rotated_square = Polygon(
    rotated_corners,
    closed=True,
    fill=False,
    edgecolor="red",
    linewidth=2,
    label="Rotated Square"
)

ax.add_patch(rotated_square)


# Mark the center
ax.plot(0, 0, "ro")


# Configure the graph
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect("equal")
ax.grid(True)

plt.title("Original vs Rotated Unit Square")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

plt.show()
