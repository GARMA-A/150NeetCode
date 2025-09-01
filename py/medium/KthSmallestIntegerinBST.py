from typing import Optional
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:  # nlogn
        if not root:
            return -1
        ctr = k
        res = root.val

        def DFS(curNode: Optional[TreeNode]):
            if not curNode:
                return
            nonlocal ctr, res
            if curNode.left:
                DFS(curNode.left)
            ctr -= 1
            if ctr == 0:
                res = curNode.val
                return
            if curNode.right:
                DFS(curNode.right)

        DFS(root)

        return res
