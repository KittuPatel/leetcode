class MinStack:

    def __init__(self):
        self.stack = []
        # (a, b) => a is val, b is minimum
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return
        current_min = self.stack[-1][1]
        
        current_min = min(current_min, val)
        self.stack.append((val, current_min))
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()