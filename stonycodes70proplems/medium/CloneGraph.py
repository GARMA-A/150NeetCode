from typing import List, Mapping, Optional
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        graph :Mapping[Node , List[Node]]={}
        visited = set()
        stack = [node]
        while stack:
            top = stack.pop()
            graph[top] = top.neighbors
            for neigbor in top.neighbors:
                if neigbor not in visited:
                    visited.add(neigbor)
                    stack.append(neigbor)
        oldToNew={}
        for origin_node in graph:
            oldToNew[origin_node] = Node(origin_node.val)

        for origin_node,neighbors in graph.items():
            oldToNew[origin_node].neighbors = [oldToNew[neighbor] for neighbor in neighbors]

        return oldToNew[node]





