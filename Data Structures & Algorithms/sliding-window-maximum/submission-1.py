class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        n = len(nums)

        res = []

        for i in range(n):
            while heap and i - heap[0][1] >= k:
                heapq.heappop(heap)
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                res.append(-heap[0][0])
        return res