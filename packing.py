
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon  # Custom 2D shapes (jaise triangle) banane ke liye class



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


# Create a unit square
corners = get_square_corner(0, 0, 1)


# Create figure and axes
fig, ax = plt.subplots()


# Draw square
square = Polygon(
    corners,
    closed=True,
    fill=False,
    edgecolor="blue",
    linewidth=2
)

ax.add_patch(square)


# Mark the center of the square
ax.plot(0, 0, "ro")


# Configure the graph
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect("equal")
ax.grid(True)

plt.title("My First Unit Square")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()


# Display the corners
for corner in corners:
    print(corner)
