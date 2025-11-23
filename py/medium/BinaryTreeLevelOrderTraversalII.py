import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque()
        queue.append(root)
        ans = []
        while queue:
            qlen = len(queue)
            level = []
            for _ in range(qlen):
                top = queue.popleft()
                level.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            ans.append(level)

        # Reverse the result to get bottom-up order
        return ans[::-1]
