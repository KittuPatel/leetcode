#User function Template for python3

class Solution:
    def solve(self,n,k,stalls):
        
        
        def isPossible(dist):
            last = stalls[0]
            cows = 1
            for i in range(1, len(stalls)):
                if stalls[i] - last >= dist:
                    cows += 1
                    last = stalls[i]
                
                if cows >= k:
                    return True
            return False
            
        
        stalls.sort()
        low, high = 1, max(stalls)
        ans = -1
        
        while low <= high:
            mid = (low+high)//2
            
            if isPossible(mid):
                ans = mid
                low = mid+1
            else:
                high = mid - 1
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends