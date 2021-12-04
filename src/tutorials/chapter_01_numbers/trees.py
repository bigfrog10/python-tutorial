from typing import List
from collections import defaultdict


# LC261. Graph Valid Tree
def validTree(self, n: int, edges: List[List[int]]) -> bool:
    if not edges: return n <= 1
    if n-1 != len(edges): return False  # a tree has to have only n-1 edges
    graph = defaultdict(list)
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    stack, seen = [0], {0}  # start from node 0
    while stack: # DFS to check is fully connected
        e = stack.pop()
        for ne in graph[e]:
            if ne not in seen:
                seen.add(ne)
                stack.append(ne)
    return len(seen) == n


# LC1490. Clone N-ary Tree
def cloneTree(self, root: 'Node') -> 'Node':
    if root is None: return None
    return Node(root.val, [self.cloneTree(child) for child in root.children])


# LC310. Minimum Height Trees - n-ary tree
def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    if n <= 2: return [i for i in range(n)] # topological sort, n-ary tree
    neighbors = defaultdict(set)
    for start, end in edges:
        neighbors[start].add(end)
        neighbors[end].add(start)
    leaves = [i for i in range(n) if len(neighbors[i]) == 1]
    while n > 2:  # topologic sort, 3 [[0,1],[0,2]] --> [0]
        n -= len(leaves)
        new_leaves = []
        for lv in leaves:
            nb = neighbors[lv].pop() # leave has only 1 neighbour - parent
            neighbors[nb].remove(lv)
            if len(neighbors[nb]) == 1: new_leaves.append(nb)
        leaves = new_leaves
    return leaves  # last leaves, could be 1 or 2 leaves


# LC1245. Tree Diameter - given graph edges
def treeDiameter(self, edges: List[List[int]]) -> int:
    graph = defaultdict(set)  # topological sort, n-ary tree
    for edge in edges:
        u, v = edge
        graph[u].add(v)
        graph[v].add(u)
    vertex_left = len(graph)
    leaves = [i for i in range(vertex_left) if len(graph[i]) == 1]
    layers = 0
    while vertex_left > 2:
        vertex_left -= len(leaves)
        next_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            if len(graph[neighbor]) == 1: next_leaves.append(neighbor)
        layers += 1
        leaves = next_leaves
    return layers * 2 + (0 if vertex_left == 1 else 1)


x = [1, 2, 3, 4, 5]
inorder_idxs = {v: i for i, v in enumerate(x)}
print(inorder_idxs)