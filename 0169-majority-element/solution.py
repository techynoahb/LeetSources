class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        ans = 0
        count = 0
        l = len(nums)

        for i in range(l):
            if count == 0 and ans != nums[i]:

                count = count + 1
                ans = nums[i]
            elif nums[i] == ans:
                count = count + 1
            else:
                count = count - 1

        return ans
