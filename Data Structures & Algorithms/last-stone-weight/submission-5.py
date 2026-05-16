class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStone = max(stones)
        
        freq = [0] * (maxStone + 1)

        for s in stones:
            freq[s] += 1
        

        r = maxStone
        while r > 0:
            if freq[r] % 2 == 0:
                r -= 1
                continue
            
            l = r - 1
            while l > 0 and freq[l] == 0:
                l -= 1
            if l == 0:
                break
            

            freq[l] -= 1
            freq[r] -= 1
            freq[r - l] += 1
            r = max(l, r - l)
        return r
