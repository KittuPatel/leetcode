class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = collections.deque()
        star = collections.deque()
        
        # step 1
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == "*":
                star.append(i)
            else:
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        
        # step 2
        while stack:
            if len(star) == 0:
                return False
            elif stack[-1] < star[-1]:
                stack.pop()
                star.pop()
            else:
                return False
                
        
        return True
        