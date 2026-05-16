class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)

        
        while len(heap) >= 2:
            heapq.heappush(heap, heapq.heappop(heap) - heapq.heappop(heap))
        
        return -heap[0]
