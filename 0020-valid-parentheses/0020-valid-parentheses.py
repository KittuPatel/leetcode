class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            ')': '(',
            '}' :'{',
            ']': '['
        }
        
        stack = collections.deque()
        
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
                
            elif char == ')' or char == '}' or char == ']':
                if len(stack) == 0 or dict[char] != stack[-1]:
                    return False
                
                else:
                    stack.pop()
                
        if len(stack) != 0:
            return False
        
        return True
        