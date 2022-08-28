class Solution:
    def isHappy(self, n: int) -> bool:
        
        def new_num(num):
            sum = 0
            while num > 0:
                num, digit = divmod(num, 10)
                sum += digit ** 2
            return sum 
        
        myset = set()
        while True:
            myset.add(n)
            n = new_num(n)

            if n == 1:
                return True

            if n in myset:
                return False

    
    