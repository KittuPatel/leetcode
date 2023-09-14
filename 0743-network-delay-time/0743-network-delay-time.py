class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = collections.defaultdict(list)
        
        # { u: [(v, w), ....]}
        for u, v, w in times:
            adjList[u].append((v, w))
        
        minHeap = [(0, k)]
        visit = set()
        t = 0
        
        while minHeap:
            w1, v1 = heapq.heappop(minHeap)
            
            if v1 in visit:
                continue
                
            visit.add(v1)
            t = max(t, w1)
            
            for n2, w2 in adjList[v1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1+w2, n2))
                    
        return t if len(visit) == n else -1
        
        