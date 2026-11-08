class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] * nums[i]

        nums.sort()
        return nums
