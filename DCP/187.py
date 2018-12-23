"""
This problem was asked by Google.
You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.
For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}
return true as the first and third rectangle overlap each other.
"""
import pprint

rects = [{
    "top_left": (1, 4),
    "dimensions": (3, 3)  # width, height
},
    {
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
    {
    "top_left": (0, 5),
    "dimensions": (4, 3)
}]


def detect_overlap(rectangles):
    rows = 5
    columns = 5
    graph = [[(x, y) for x in range(-rows, columns + 1)] for y in range(rows, -columns - 1, -1)]

    rectangs = {}
    for rect in rectangles:
      rectangs[rect['top_left']] = [(x, y) for x in range(rect['top_left'][0], rect['dimensions'][0]) for y in range(rect['top_left'][1] - 1, -rect['dimensions'][1] - 1, -1)]

    pprint.pprint(rectangs) 



    # count = 1
    # for rect in rectangles:
    #     top_left = rect['top_left']
    #     dimensions = rect['dimensions']

    #     for row in graph:
    #         for col in row:
    #             if col == top_left:
    #                 print('here', graph[graph.index(row)][row.index(col)])
    #                 graph[graph.index(row)][row.index(col)] = ('-', '-')
    #     count +=1

    for row in graph:
        print(row)


print(detect_overlap(rects))
