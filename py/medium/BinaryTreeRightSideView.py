from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def DFS(curNode, depth):
            if not curNode:
                return
            if len(ans) == depth:
                ans.append(curNode.val)

            DFS(curNode.right, depth + 1)
            DFS(curNode.left, depth + 1)

        DFS(root, 0)

        return ans
