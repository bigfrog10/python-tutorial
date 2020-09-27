import heapq


# this class is the same as the maze one, so can be folded into one.
class Node:
    def __init__(self, value, parent: 'Node' = None):
        self.value = value
        self.parent = parent

        # cost function f
        self.cost = 0 if parent is None else parent.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.__class__.__name__ == other.__class__.__name__ and\
            self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return f"({self.value}, {self.cost})"


def _is_shorter(promisings, next_node):
    for n in promisings:
        if n == next_node and n.cost <= next_node.cost:
            return False
    return True


def _get_path(node):
    path = []
    while node.parent is not None:  # not the first node
        path.append((node.value, node.cost))
        node = node.parent

    path.append(node)  # first node
    return path[::-1]


def dijkstra_search(adjacent_matrix):
    # use adjacent_matrix to represent graph. adjacent_matrix for undirected
    # graph is symmetric. 0 in adjacent_matrix means no path, all weights > 0.
    # we assume the adjcent_matrix size is the number of nodes in the graph.
    # The nodes are labeled as 0 ... size.
    # we assume the first node 0 is the start and the last node size - 1 is the
    # destination/end.
    size = len(adjacent_matrix)
    promisings = []
    visited = set()

    heapq.heappush(promisings, Node(0))  # 0 is the start node
    while promisings:
        node = heapq.heappop(promisings)  # smallest by the order
        visited.add(node.value)
        print(f"node={node}, size={len(promisings)}")

        if node.value == size - 1:  # target node
            return _get_path(node)

        # find next node
        for n in range(size):  # loop all nodes
            if n not in visited and adjacent_matrix[node.value][n] > 0:
                next_node = Node(n, node)
                next_node.cost += adjacent_matrix[node.value][n]
                if _is_shorter(promisings, next_node):  # this is the core logic
                    heapq.heappush(promisings, next_node)

    return None


def _test1():
    am = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]

    path = dijkstra_search(am)
    print(path)


def _test2():
    am = [
        [0,  7,  9,  0, 14, 0],
        [7,  0, 10, 15,  0, 0],
        [9, 10,  0, 11,  2, 0],
        [0, 15, 11,  0,  0, 6],
        [14, 0,  2,  0,  0, 9],
        [0,  0,  0,  6,  9, 0],
    ]

    path = dijkstra_search(am)
    print(path)


if __name__ == '__main__':
    import cProfile
    cProfile.run('_test2()')

# use networkx to print a graph

# https://www.educative.io/edpresso/how-to-implement-dijkstras-algorithm-in-python
# https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
# https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
#

# https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm for negative weights
