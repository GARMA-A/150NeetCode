from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        ans = float("inf")
        prevNode = None
        def inorder(root:Optional[TreeNode]):
            nonlocal ans , prevNode

            if not root:
                return None
            inorder(root.left)
            if prevNode:
                 ans = min(ans , abs(prevNode.val - root.val))
            prevNode  = root
            inorder(root.right)
        inorder(root)
        return int(ans)



