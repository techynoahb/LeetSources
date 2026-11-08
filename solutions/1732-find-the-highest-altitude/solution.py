class Solution:
    def largestAltitude(self, gain: list[int]) -> int:

        n = len(gain)
        alt = 0
        netAlt = 0

        for i in range(0,n):
            netAlt += gain[i]
            alt = max(alt, netAlt)
        return alt
