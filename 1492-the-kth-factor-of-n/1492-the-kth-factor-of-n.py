class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        # 1 2 3 4 5 6 .... n
        count = 0
        for i in range(1, n+1):
            if n%i == 0:
                count+=1
                if count == k:
                    return i
            
        if k > count:
            return -1
        
        return fact_list[k-1]