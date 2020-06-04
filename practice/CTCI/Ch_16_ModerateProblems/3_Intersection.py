"""
Given two straight line segments (represented as a start and an end point), compute the point of intersection, if any.
"""


def check_slopes(line1, line2):
    """
    Calculate the slope for each
    """
    slope_1 = (line1[1][1] - line1[0][1]) // (line1[1][0] - line1[0][0])
    slope_2 = (line2[1][1] - line2[0][1]) // (line2[1][0] - line2[0][0])

    if slope_1 != slope_2:
        return True
    else:
        return False


def check_ranges(line1, line2):

    min_y_line1 = min(line1[0][1], line1[1][1])
    max_y_line1 = max(line1[0][1], line1[1][1])
    min_y_line2 = min(line2[0][1], line2[1][1])
    max_y_line2 = max(line2[0][1], line2[1][1])
    min_x_line1 = min(line1[0][0], line1[1][0])
    max_x_line1 = max(line1[0][0], line1[1][0])
    min_x_line2 = min(line2[0][0], line2[1][0])
    max_x_line2 = max(line2[0][0], line2[1][0])

    if min_y_line1 > max_y_line2 or min_y_line2 > max_y_line1 or min_x_line1 > max_x_line2 or min_x_line2 > max_x_line1:
        return False

    return True


def find_intersection(line1, line2):
    print('Line 1: {}'.format(line1))
    print('Line 2: {}'.format(line2))
    return check_slopes(line1, line2) and check_ranges(line1, line2)


line_1 = [(-1, 1), (2, 4)]
line_2 = [(-1, 5), (2, 2)]
print(find_intersection(line_1, line_2))
