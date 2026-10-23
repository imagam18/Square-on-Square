
import math


def get_square_corners(center_x, center_y, angle_radians):
    """Calculate the four corners of a unit square."""

    cosine_angle = math.cos(angle_radians)
    sine_angle = math.sin(angle_radians)

    # Corner coordinates relative to the square's center
    local_corner_offsets = [
        (-0.5, -0.5),
        ( 0.5, -0.5),
        ( 0.5,  0.5),
        (-0.5,  0.5),
    ]

    absolute_corners = []

    for offset_x, offset_y in local_corner_offsets:
        # Rotate the corner around the center, then translate it.
        corner_x = (
            center_x
            + offset_x * cosine_angle
            - offset_y * sine_angle
        )

        corner_y = (
            center_y
            + offset_x * sine_angle
            + offset_y * cosine_angle
        )

        absolute_corners.append((corner_x, corner_y))

    return absolute_corners


def get_container_side_length(squares):
    """Find the side length of the smallest axis-aligned
    square that encloses all the given squares."""

    all_corners = []

    for center_x, center_y, angle_radians in squares:
        corners = get_square_corners(
            center_x, center_y, angle_radians
        )
        all_corners.extend(corners)

    minimum_x = min(x for x, y in all_corners)
    maximum_x = max(x for x, y in all_corners)
    minimum_y = min(y for x, y in all_corners)
    maximum_y = max(y for x, y in all_corners)

    total_width = maximum_x - minimum_x
    total_height = maximum_y - minimum_y

    return max(total_width, total_height)


def project_corners_onto_axis(corners, axis):
    """Find the minimum and maximum projections onto an axis."""

    projected_values = [
        corner_x * axis[0] + corner_y * axis[1]
        for corner_x, corner_y in corners
    ]

    minimum_projection = min(projected_values)
    maximum_projection = max(projected_values)

    return minimum_projection, maximum_projection


def get_edge_normal_axes(corners):
    """Get perpendicular axes for all four square edges."""

    perpendicular_axes = []

    for edge_index in range(4):
        start_x, start_y = corners[edge_index]
        end_x, end_y = corners[(edge_index + 1) % 4]

        edge_x = end_x - start_x
        edge_y = end_y - start_y

        # Rotate the edge vector by 90 degrees.
        normal_x = -edge_y
        normal_y = edge_x

        perpendicular_axes.append((normal_x, normal_y))

    return perpendicular_axes


def do_squares_overlap(square_a, square_b, epsilon=1e-10):
    """Return True if the squares have positive-area overlap."""

    corners_a = get_square_corners(*square_a)
    corners_b = get_square_corners(*square_b)

    candidate_axes = (
        get_edge_normal_axes(corners_a)
        + get_edge_normal_axes(corners_b)
    )

    for axis in candidate_axes:
        minimum_a, maximum_a = project_corners_onto_axis(
            corners_a, axis
        )
        minimum_b, maximum_b = project_corners_onto_axis(
            corners_b, axis
        )

        overlap_length = (
            min(maximum_a, maximum_b)
            - max(minimum_a, minimum_b)
        )

        if overlap_length <= epsilon:
            return False

    return True


if __name__ == "__main__":
    # One unit square
    one_square_packing = [(0.0, 0.0, 0.0)]
    print(
        "One square:",
        get_container_side_length(one_square_packing)
    )

    # Two squares touching along an edge
    first_square = (0.0, 0.0, 0.0)
    second_square = (1.0, 0.0, 0.0)

    print(
        "Touching:",
        do_squares_overlap(first_square, second_square)
    )

    # Two squares whose interiors overlap
    overlapping_square = (0.5, 0.0, 0.0)

    print(
        "Overlapping:",
        do_squares_overlap(first_square, overlapping_square)
    )
