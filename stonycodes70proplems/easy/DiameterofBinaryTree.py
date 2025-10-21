from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root,False)]
        diameter = 0
        mp = {}
        while stack:
            node ,visited = stack.pop()
            if not visited:
                stack.append((node,True))
                if node.left:
                    stack.append((node.left , False))
                if node.right:
                    stack.append((node.right , False))
            else:
                left_height , right_height = 0 , 0
                if not node.left:
                    left_height = 0
                else:
                    left_height = mp.pop(node.left)
                if not node.right:
                    right_height = 0
                else:
                    right_height = mp.pop(node.right)
                diameter = max(diameter , left_height+right_height)
                mp[node] = 1+max(left_height,right_height)


        return diameter






