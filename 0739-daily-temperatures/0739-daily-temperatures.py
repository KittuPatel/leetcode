class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in temperatures]
        
        stack.append(0)
        
        for i in range(1, len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                popped = stack.pop()
                result[popped] = i - popped
            
            stack.append(i)
            
        return result