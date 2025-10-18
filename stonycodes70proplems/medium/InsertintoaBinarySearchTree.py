from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        if not root :
            return newNode

        if root.val < val and root.right:
            self.insertIntoBST(root.right , val)
        elif root.val < val and not root.right:
            root.right = newNode


        if root.val > val and root.left:
            self.insertIntoBST(root.left , val)
        elif root.val > val and not root.left:
            root.left = newNode

        return root

