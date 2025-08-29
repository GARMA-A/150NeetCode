from typing import Optional, Set


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        oldToNew = {}

        def DFS(node: Node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nie in node.neighbors:
                copy.neighbors.append(DFS(nie))
            return copy

        return DFS(node)
