from typing import List, Optional
from collections import deque

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
# DFS solution
class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

# BFS solution
class Solution: 
    def sortedArrayToBST(self , nums:List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        d = deque()
        d.append((root,0,mid-1))
        d.append((root,mid+1,len(nums)-1))
        while d:
            parent , left , right = d.popleft()
            if left <=right:
                mid = (left+right)//2
                child = TreeNode(nums[mid])
                if parent.val >child.val:
                    parent.left = child
                else:
                    parent.right = child
                d.append((child , left , mid-1))
                d.append((child , mid+1 , right))
        return root













