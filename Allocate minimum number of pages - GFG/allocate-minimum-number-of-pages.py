class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        
        def isPossible(pagesCount):
            curSum = 0
            booksAllocCount = 0
            for i in range(len(A)):
                if curSum + A[i] <= pagesCount:
                    curSum += A[i]
                else:
                    booksAllocCount += 1
                    curSum = A[i]
            
            booksAllocCount += 1  # Count the last student.
            
            if booksAllocCount <= M:
                return True
            return False
                    
                
        
        low = max(A)
        high = sum(A)
        
        if N < M:
            return -1
        ans = 0
        
        while low <= high:
            mid = (low+high)//2
            if isPossible(mid):
                ans = mid
                high = mid -1
            else:
                low = mid+1
        
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends