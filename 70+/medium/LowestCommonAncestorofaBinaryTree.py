from collections import deque
from typing import Mapping , Set

class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        d= deque([root])
        parents = {root:None}

        while d:
            node = d.popleft()
            if node.left:
                d.append(node.left)
                parents[node.left] = node #type:ignore
            if node.right:
                d.append(node.right)
                parents[node.right] = node #type:ignore
            if p in parents and q in parents:
                break

        accessors = set()
        while q:
            accessors.add(q)
            q = parents[q] #type:ignore

        while p:
            if p in accessors:
                return p
            p = parents[p]


        return root








