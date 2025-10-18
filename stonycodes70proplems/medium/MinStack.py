class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min_st or self.min_st[-1]>=val:
            self.min_st.append(val)

    def pop(self) -> None:
        if not self.st:
            return None
        top = self.st.pop()
        if self.min_st and top == self.min_st[-1]:
            self.min_st.pop()

    def top(self) -> int:
        if not self.st :
            raise IndexError("stack is empty")
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1] if len(self.min_st) else 0



obj = MinStack()
obj.push(1)
obj.push(-1)
obj.push(0)
print(obj.getMin())
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.getMin())
