class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            dif = target - n
            if dif in map:
                return [map[dif], i]
            map[n] = i
        return []