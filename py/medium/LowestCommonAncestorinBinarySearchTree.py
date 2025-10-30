class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val < q.val and root.val < p.val and root.right:
            return self.lowestCommonAncestor(root.right , p ,q)
        elif root.val > q.val and root.val > p.val and root.left:
            return self.lowestCommonAncestor(root.left , p , q)
        else:
            return root
        
        
