class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        countT = defaultdict(int)
        countS = defaultdict(int)

        for c in t:
            countT[c] += 1
        target = len(countT)
        

        res = [-1, -1]
        resLen = float('inf')
        l = cur = 0
        for r in range(len(s)):
            c = s[r]
            countS[c] += 1
            if countS[c] == countT[c]:
                cur += 1
            while cur == target:
                if resLen > r - l + 1:
                    resLen = r - l + 1
                    res = [l, r + 1]
                c = s[l]
                countS[c] -= 1
                if countS[c] + 1 == countT[c]:
                    cur -= 1
                l += 1
        
        l, r = res
        return s[l:r] if resLen != float('inf') else ""
