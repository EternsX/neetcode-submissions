class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                val = height[stack.pop()]
                if stack:
                    l = height[stack[-1]]
                    r = height[i]
                    h = min(l, r) - val
                    width = i - stack[-1] - 1
                    res += h * width
            stack.append(i)
        return res

            