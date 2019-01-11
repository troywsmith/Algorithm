"""
A monochrome screen is stored as a single array of bytes, allowing eight consecutive pixels to be stored in one byte.
The screen has width w, where w is divisible by 8.
The height of the screen can be derived from the length of the array and the width
Implement a function that draws a horizontal line from (x1,y) to (x2,y)
"""


def stringify_screen(screen, width):

    string = ''
    height = len(screen) * 8 // width

    for h in range(0, height):
        string += '\n'

        for w in range(0, width // 8):
            string += format(screen[h * width // 8 + w], '#010b')[2:]

    return string


def single_byte_line(x1, x2):

    num_1s = x2 - x1 + 1
    byte = 1

    while num_1s > 1:
        byte <<= 1
        byte += 1
        num_1s -= 1

    left_shift = 8 - x2 - 1
    byte <<= left_shift
    return byte


def draw_line(screen, width, x1, x2, y):

    x1_byte_index = y * width // 8 + x1 // 8
    x2_byte_index = y * width // 8 + x2 // 8

    if x1_byte_index == x2_byte_index:
        screen[x1_byte_index] = single_byte_line(x1 % 8, x2 % 8)
    else:

        # draw 1s from x1 to end of its byte
        screen[x1_byte_index] = single_byte_line(x1 % 8, 7)

        # draw 1s from 0 to x2 in its byte
        screen[x2_byte_index] = single_byte_line(0, x2 % 8)

    for index in range(x1_byte_index + 1, x2_byte_index):
        screen[index] = 255
