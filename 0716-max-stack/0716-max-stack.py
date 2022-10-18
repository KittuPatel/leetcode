from sortedcontainers import SortedList

class MaxStack:

    def __init__(self):
        self.stack = SortedList()
        self.maximum = SortedList()
        self.id = 0

    def push(self, x: int) -> None:
        self.stack.add((self.id, x))
        self.maximum.add((x, self.id))
        self.id += 1

    def pop(self) -> int:
        i, x = self.stack.pop()
        self.maximum.remove((x, i))
        return x

    def top(self) -> int:
        return self.stack[-1][1]

    def peekMax(self) -> int:
        return self.maximum[-1][0]

    def popMax(self) -> int:
        x, i = self.maximum.pop()
        self.stack.remove((i, x))
        return x



# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()