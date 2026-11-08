class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        l = len(nums)   
        nums.sort()

        #note, tried just searching through without sorting first, sorting makes it slower but makes solution easier

        for i in range(0,l-1,1):
            if nums[i] == nums[i+1]:
                return True
        return False
