class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            m = l + (r - l) // 2

            k = 0
            for p in piles:
                k += math.ceil(p / m)
            
            if k <= h:
                r = m
            else:
                l = m + 1
        return l
