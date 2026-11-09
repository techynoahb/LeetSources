class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        cnt = 0
        for i in range(len(arr1)):
            is_valid = True             
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    is_valid = False     

            if is_valid:
                cnt += 1
        return cnt
