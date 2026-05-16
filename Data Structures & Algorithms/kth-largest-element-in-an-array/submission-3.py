import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k -= 1

        l, r = 0, len(nums) - 1

        while True:
            pivot_idx = random.randint(l, r)

            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            pivot = nums[r]

            p = l

            for i in range(l, r):
                if nums[i] >= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if p == k:
                return nums[p]
            elif p < k:
                l = p + 1
            else:
                r = p - 1