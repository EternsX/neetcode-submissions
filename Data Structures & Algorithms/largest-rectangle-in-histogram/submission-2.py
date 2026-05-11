class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        res = 0

        for i in range(n):
            start = i
            while stack and heights[stack[-1][1]] >= heights[i]:
                [start, idx] = stack.pop()
                h = heights[idx]
                width = i - start 
                res = max(res, h * width)

            stack.append((start, i))
        print(stack)
        for (start, i) in stack:
            res = max(res, (n - start) * heights[i])
        return res 