class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        res = []
        dict = {}
        
        for idx, grp in enumerate(groupSizes):
            if grp not in dict:
                dict[grp] = [idx]
            else:
                dict[grp].append(idx)

            if len(dict[grp]) == grp:
                res.append(dict[grp])
                del dict[grp]
        return res
            
