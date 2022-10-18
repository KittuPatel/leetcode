class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxHeap = []
        self.poppedIdxs = set()
        self.i = 0
        # Time: O(1)
        # Space: O(1)

    def push(self, x: int) -> None:
        self.stack.append((x, self.i))
        heappush(self.maxHeap, (-x, -self.i))
        self.i += 1
        # Time: O(1) amortized per each of the n calls made
        # Space: O(1) amortized per each of the n calls made

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.poppedIdxs:
            self.stack.pop()
        self.poppedIdxs.add(self.stack[-1][1])
        return self.stack.pop()[0]
        # Time: O(1) amortized, for each call
        # Space: O(1)
        
    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.poppedIdxs:
            self.stack.pop()
        if self.stack:
            return self.stack[-1][0]
        # Time: O(1)
        # Space: O(1)

    def peekMax(self) -> int:
        while self.maxHeap and -self.maxHeap[0][1] in self.poppedIdxs:
            heappop(self.maxHeap)
        if self.maxHeap:
            return -self.maxHeap[0][0]
        # Time: O(log(n)) where n is the length of maxHeap
        # Soace: O(1)

    def popMax(self) -> int:
        if len(self.maxHeap) == 0:
            return
        while self.maxHeap and -self.maxHeap[0][1] in self.poppedIdxs:
            heappop(self.maxHeap)
        popped = heappop(self.maxHeap)
        x, i = popped
        x, i = -x, -i
        self.poppedIdxs.add(i)
        return x
        # Time: O(log(n)) where n is the length of maxHeap
        # Soace: O(1)


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()