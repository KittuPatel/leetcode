class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        lookup = {i: (src, tgt) for i, src, tgt in zip(indices, sources, targets)}
        i, result = 0, ""
        while i < len(s):
            if i in lookup and s[i:].startswith(lookup[i][0]):
                result += lookup[i][1]
                i += len(lookup[i][0])
            else:
                result += s[i]
                i += 1
        return result