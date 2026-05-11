class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        prevMap = defaultdict(int)

        res = 0
        for n in nums:
            if not prevMap[n]:
                prevMap[n] = prevMap[n - 1] + prevMap[n + 1] + 1
                prevMap[n - prevMap[n - 1]] = prevMap[n]
                prevMap[n + prevMap[n + 1]] = prevMap[n]
                res = max(res, prevMap[n])
        return res
