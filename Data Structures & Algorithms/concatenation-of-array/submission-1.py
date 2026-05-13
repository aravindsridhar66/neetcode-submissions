class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2*n)
        for index, i in enumerate(nums):
            ans[index] = ans[index+n] = i

        return ans