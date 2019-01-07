def find_greatest_stack_height(boxes):

    # Initialize highest stack to largest negative number
    highest_stack_height = float('-inf')
    highest_stack = []

    # Sort Boxes by height
    sorted_boxes = sort_boxes(boxes)

    # Find possible stacks with each box at the bottom
    for i, base_box in enumerate(sorted_boxes):

        # print('Base Box: {}'.format(base_box))
        stack = [base_box]
        boxes_remaining = boxes[:i] + boxes[i+1:]
        max_width = base_box[0]
        max_height = base_box[1]
        max_depth = base_box[2]

        build_stack(stack, boxes_remaining, max_width, max_height, max_depth)

        height = get_height(stack)

        # If height of stack is greater than the current highest, set it to the highest
        if height > highest_stack_height:
            highest_stack = stack
            highest_stack_height = height

        # print(' ')

    # Return the highest stack
    return (highest_stack_height, highest_stack)


def sort_boxes(boxes):
    return boxes


def build_stack(stack, boxes_remaining, max_width, max_height, max_depth):

    # print('Stack: {}'.format(stack))
    # print('Boxes Remaining: {}'.format(boxes_remaining))
    # print('Max Width: {}'.format(max_width))
    # print('Max Height: {}'.format(max_height))
    # print('Max Depth: {}'.format(max_depth))

    # Base Case
    if len(boxes_remaining) <= 1:
        return stack

    # Recursively build stack
    for i, box in enumerate(boxes_remaining):

        if box[0] < max_width and box[1] < max_height and box[2] < max_depth:
            # print('Box: {} is a valid option'.format(box))
            stack.append(box)
            boxes_remaining = boxes_remaining[:i] + boxes_remaining[i+1:]
            max_width = box[0]
            max_height = box[1]
            max_depth = box[2]
            build_stack(stack, boxes_remaining,
                        max_width, max_height, max_depth)
        # else:
        #     print('Box: {} is not a valid option'.format(box))


def get_height(stack):
    height = 0
    for box in stack:
        height += box[1]
    return height


if __name__ == '__main__':
    boxes = [(343, 25, 46), (11, 56, 32), (22, 63, 424), (43, 34, 765)]

    greatest_stack = find_greatest_stack_height(boxes)
    print('Greatest Stack Height: {}'.format(greatest_stack[0]))
    print('Greatest Stack: {}'.format(greatest_stack[1]))
