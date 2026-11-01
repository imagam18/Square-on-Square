import streamlit as st
import matplotlib.pyplot as plt

from matplotlib.patches import Polygon
from core.geometry import get_rotated_square


st.set_page_config(
    page_title="Squares in Squares Studio",
    layout="wide"
)

st.title("Squares in Squares Studio")

st.write(
    "Visualize and experiment with unit square packing."
)

# Sidebar controls
st.sidebar.header("Packing Settings")

number_of_squares = st.sidebar.slider(
    "Number of squares",
    min_value=1,
    max_value=10,
    value=5
)

# Sample square positions
sample_squares = [
    (0, 0, 0),
    (1.5, 0, 0.3),
    (3, 0, 0.6),
    (0, 1.5, 0.9),
    (1.5, 1.5, 1.2),
    (3, 1.5, 0.2),
    (0, 3, 0.5),
    (1.5, 3, 0.8),
    (3, 3, 1.1),
    (4.5, 3, 0.4)
]

fig, ax = plt.subplots(figsize=(8, 8))

for i in range(number_of_squares):

    cx, cy, angle = sample_squares[i]

    corners = get_rotated_square(
        cx,
        cy,
        angle
    )

    square = Polygon(
        corners,
        closed=True,
        fill=False,
        linewidth=2
    )

    ax.add_patch(square)

    ax.plot(cx, cy, "ro")

    ax.text(cx, cy, str(i + 1))

ax.set_xlim(-1, 6)
ax.set_ylim(-1, 5)

ax.set_aspect("equal")
ax.grid(True)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Square Packing Visualization")

st.pyplot(fig)
plt.close(fig)

st.success(
    f"Displaying {number_of_squares} squares"
)