from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        def inorder(root:Optional[TreeNode]):
            if not root or len(stack)>=k:
                return None
            inorder(root.left)
            if len(stack) < k:
                stack.append(root.val)
            inorder(root.right)
        inorder(root)

        return stack.pop()
















