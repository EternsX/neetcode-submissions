class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k -= 1

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] >= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            return p
            
        
        P = len(nums)
        L, R = 0, len(nums) - 1
        while P != k:
            P = quickSelect(L, R)

            if P < k:
                L = P + 1
            elif P > k:
                R = P - 1
        return nums[k]


