from typing import List


class Solution:
    def sortStack(self, stack:List[int])->List[int]:
        temp_stack , temp_num= [] ,0
        temp_num = stack.pop()
        while stack:
            if not temp_stack or temp_num < temp_stack[-1]:
                temp_stack.append(temp_num)
                temp_num = stack.pop() 
            else:
                stack.append(temp_stack.pop())
        return temp_stack

s  = Solution()
print(s.sortStack([34,3,31,98,92,23]))
