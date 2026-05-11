class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        res = 0

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                idx = stack.pop()
                h = heights[idx]
                width = i - stack[-1] - 1 if stack else i
                res = max(res, h * width)
            stack.append(i)
        return res

