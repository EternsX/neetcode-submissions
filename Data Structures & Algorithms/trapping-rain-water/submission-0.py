class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        maxL = maxR = 0
        while l < r:
            if height[l] < height[r]:
                maxL = max(height[l], maxL)
                res += maxL - height[l]
                l += 1
            else:
                maxR = max(height[r], maxR)
                res += maxR - height[r]
                r -= 1
        return res

            