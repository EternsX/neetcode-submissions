class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        p = l

        l, r = 0, len(nums) - 1
        if nums[p] <= nums[r] and nums[r] >= target:
            l = p
        else:
            r = p - 1
        
        while l <= r:
            m = l + (r - l) // 2
            print(m)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1