from collections import deque
from typing import List, Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(root:Optional[TreeNode]):
            if not root:
                return None
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        newRoot  = self.balance( arr)
        return newRoot

    def balance(self , arr:List[int])->Optional[TreeNode]:
        mid = len(arr)//2
        q  = deque()
        myRoot = TreeNode(arr[mid])
        q.append((myRoot , 0, mid-1))
        q.append((myRoot ,mid+1 , len(arr)-1))
        while q:
            parent , left , right = q.popleft()
            if left<=right:
                mid = (left+right)//2
                child = TreeNode(arr[mid])
                if child.val < parent.val:
                    parent.left = child
                else:
                    parent.right = child
                q.append((child , left , mid-1))
                q.append((child , mid+1 , right))

        return myRoot

