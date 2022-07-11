class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        max_element = 0
        for i in range(len(arr)):
            if i != len(arr) - 1:
                max_value = max(arr[i+1:len(arr)])
                arr[i] = max_value
            else:
                arr[i] = -1
        
        return arr