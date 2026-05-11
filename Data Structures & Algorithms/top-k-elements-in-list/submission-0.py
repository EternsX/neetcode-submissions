class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        res = [[] for _ in range(len(nums) + 1)]
        
        print(count)
        for n in count:
            res[count[n]].append(n)
        
        output = []
        for values in res[::-1]:
            for v in values:
                output.append(v)
                if len(output) >= k:
                    return output
        return output