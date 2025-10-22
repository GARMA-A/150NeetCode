from typing import Optional 
from collections import deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

#BFS
class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        copy = {node:Node(node.val)}
        queue = deque([node])
        while queue:
            current = queue.popleft()
            for nei in current.neighbors:
                if nei not in copy:
                    queue.append(nei)
                    copy[nei] = Node(nei.val)
                copy[current].neighbors.append(copy[nei])
        return copy[node]



#DFS
class Solution2:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        deepClone = {node:Node(node.val)}
        stack = [node]
        while stack:
            current = stack.pop()
            for nei in current.neighbors:
                if nei not in deepClone:
                    deepClone[nei] = Node(nei.val)
                    stack.append(nei)
                deepClone[current].neighbors.append(deepClone[nei])
        return deepClone[node]











