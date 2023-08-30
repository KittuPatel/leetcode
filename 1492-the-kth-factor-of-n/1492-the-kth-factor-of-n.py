class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        # 1 2 3 4 5 6 .... n
        fact_list = []
        for i in range(1, n+1):
            if n%i == 0:
                fact_list.append(i)
            
        if k > len(fact_list):
            return -1
        
        return fact_list[k-1]