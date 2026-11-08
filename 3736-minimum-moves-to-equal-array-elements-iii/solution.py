class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxNum = max(nums)
        ans = 0
        for i in range(len(nums)):
            ans += maxNum - nums[i]
        return ans
