class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        result = []
        mList = list(range(1, m+1))
        
        for x in queries:
            result.append(mList.index(x))
            mList.remove(x)
            mList.insert(0, x)
        
        # return the stored index result of queries
        return result