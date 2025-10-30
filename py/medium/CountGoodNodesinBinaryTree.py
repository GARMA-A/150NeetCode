from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        mx = root.val
        ans = 0
        def DFS(root:Optional[TreeNode] , mx :int):
            if not root:
                return 
            nonlocal ans
            if root.val >= mx:
                ans+=1
                mx = root.val
            DFS(root.left , mx)
            DFS(root.right , mx)
        DFS(root , mx)
        return ans




