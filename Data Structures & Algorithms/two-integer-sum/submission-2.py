class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in h:
                return [h[diff], index]
            else:
                h[num] = index