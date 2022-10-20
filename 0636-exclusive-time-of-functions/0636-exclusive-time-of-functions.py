class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ftimes = [0] * n
        stack = []
        prev_start_time = 0
        
        for log in logs:
            fid, typ, timestamp = log.split(":")
            fid, timestamp = int(fid), int(timestamp)
            
            if typ == "start":
                if stack:
                    ftimes[stack[-1]] += timestamp - prev_start_time
                stack.append(fid)
                prev_start_time = timestamp
                
            else:
                idFromStack = stack.pop()
                ftimes[idFromStack] += timestamp - prev_start_time + 1
                prev_start_time = timestamp + 1 
        
        return ftimes