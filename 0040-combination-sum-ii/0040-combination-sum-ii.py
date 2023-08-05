class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()  # Sort the candidates to handle duplicates
        result = []
            
        def combinationSum2Helper(pos, target, curComb, result):
            if target == 0:
                result.append(curComb[:])
            if target <= 0:
                return
            
            for i in range(pos, len(candidates)):
                if candidates[i] == candidates[i-1] and i > pos:
                    continue
                curComb.append(candidates[i])
                combinationSum2Helper(i+1, target-candidates[i], curComb, result)
                curComb.pop()
        
        combinationSum2Helper(0, target, [], result)
        return result
            
            