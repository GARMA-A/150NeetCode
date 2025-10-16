from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []

        def DFS(root:Optional[TreeNode]):
            if not root:
                return 
            DFS(root.left)
            arr.append(root.val)
            DFS(root.right)
        DFS(root)

        if len(arr)<2:
            return False

        left ,right = 0 , len(arr)-1
        while left<right:
            if (arr[left]+arr[right])<k:
                left+=1
            elif(arr[left]+arr[right])>k:
                right-=1
            else:
                return True
        return False



s = Solution()

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

s.findTarget(root,9)



