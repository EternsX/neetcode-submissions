class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res = maxCount = 0

        seen = defaultdict(int)
        for r in range(len(s)):
            seen[s[r]] += 1
            maxCount = max(maxCount, seen[s[r]])
            print(l, r, maxCount)
            if r - l + 1 - maxCount > k:
                seen[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
            

            