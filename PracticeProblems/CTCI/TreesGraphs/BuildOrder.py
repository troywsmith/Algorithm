
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, name):
        self.name = name
        self.in_degree = 0
        self.children = []
        self.parents = []


def findBuildOrder(projects, dependencies):
    """
    Determing a build order given a list of projects and their dependencies
    """

    build_list = []  # initialize build order list
    nodes_dict = {}

    # convert string representation of project to nodes
    for project_name in projects:
        nodes_dict[project_name] = Node(project_name)

    # convert string representation of dependencies to edges between nodes
    for dep in dependencies:
        nodes_dict[dep[0]].children.append(
            nodes_dict[dep[1]])  # parent -> child
        nodes_dict[dep[1]].parents.append(
            nodes_dict[dep[0]])  # child <- parent
        nodes_dict[dep[1]].in_degree += 1

    # Kahn's algorithm for topological sorting
    q = Queue()
    for name in projects:  # place every node with 0 in_degree in queue
        node = nodes_dict[name]
        if node.in_degree == 0:
            build_list.append(node.name)
            q.enqueue(node)

    while not q.isEmpty():
        current = q.dequeue()
        for child_node in current.children:
            child_node.in_degree -= 1  # reduce in degree once parent is removed from queue
            if child_node.in_degree == 0:  # check if in_degree is 0
                build_list.append(child_node.name)
                q.enqueue(child_node)

    if len(build_list) != len(projects):
        return None

    return build_list


if __name__ == '__main__':

    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

    print('Following is an accurate build order of the given projects')
    order = findBuildOrder(projects, dependencies)
    print(order)
    # for project in order:
    #     print(project.name)
