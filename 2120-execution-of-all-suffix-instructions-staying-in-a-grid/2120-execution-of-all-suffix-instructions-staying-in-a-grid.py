class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:

        ans = []

        for startIndex in range(len(s)):
            totalSteps = 0
            r, c = startPos

            for stepIndex in range(startIndex, len(s)):
                step = s[stepIndex]

                if step == 'L':
                    c -= 1
                elif step == 'R':
                    c += 1
                elif step == 'U':
                    r -= 1
                else:
                    r += 1

                if r < 0 or r >= n or c < 0 or c >= n:
                    ans.append(totalSteps)
                    break

                totalSteps += 1
            else:
                ans.append(totalSteps)

        return ans