from collections import deque
from typing import Deque
class MyStack:

    def __init__(self):
        self.dq :Deque[int]= deque()
        

    def push(self, x: int) -> None:
        self.dq.append(x)
        

    def pop(self) -> int:
        return self.dq.pop()
        

    def top(self) -> int:
        return self.dq[-1]
        

    def empty(self) -> bool:
        return False if self.dq else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
