class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        res = []
        wealth = 0

        row = len(accounts)
        col = len(accounts[0])
        
        for i in range(row):
            wealth = 0
            for j in range(col):
                wealth += accounts[i][j]
            res.append(wealth)
        return max(res)

#time comp is O(m x n) cause we are just summing through the cols, pretty much the simplest approach
