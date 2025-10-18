from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right , key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                 replacementNode= self.replacementNode(root.right)
                 root.val = replacementNode.val
                 root.right = self.deleteNode(root.right , replacementNode.val)
        return root

    def replacementNode(self , root:Optional[TreeNode])->Optional[TreeNode]:
        cur = root
        while cur.left:
            cur = cur.left
        return cur

