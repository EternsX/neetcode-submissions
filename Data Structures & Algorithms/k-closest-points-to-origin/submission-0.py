class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean = lambda x, y: (x * x) + (y * y)

        heap = []

        for x, y in points:
            heapq.heappush(heap, (-euclidean(x, y), [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)

        return [heap[i][1] for i in range(k)]
        
