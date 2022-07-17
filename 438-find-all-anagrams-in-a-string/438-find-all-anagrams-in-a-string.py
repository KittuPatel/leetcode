class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        k = len(p)
        res = []
        d = {}
        for i in p:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        i = 0
        j = 0
        count = len(d)



        while j < n:
            if s[j] in d:
                d[s[j]] -= 1
                if d[s[j]] == 0:
                    count -= 1
            if (j-i+1) < k:
                j += 1
            elif (j-i+1) == k:
                if count == 0:
                    res.append(i)

                if s[i] in d:
                    d[s[i]] += 1
                    if d[s[i]] == 1:
                        count += 1

                i += 1
                j += 1
        return res