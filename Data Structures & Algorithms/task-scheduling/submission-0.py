class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for t in tasks:
            count[t] += 1
        
        heap = []
        for t in count:
            heapq.heappush(heap, (-count[t]))
        



        q = deque([])
        time = 0
        while heap or q:
            if heap:
                t = 1 + heapq.heappop(heap)
                if t:
                    q.append((time + n, t))
            
            if q and q[0][0] == time:
                heapq.heappush(heap, q.popleft()[1])
            time += 1
        return time
