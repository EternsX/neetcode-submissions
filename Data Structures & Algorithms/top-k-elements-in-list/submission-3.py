class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if (len(heap) > k):
                heapq.heappop(heap)
        

        res = []
        for i, n in heap:
            res.append(n)
        return res