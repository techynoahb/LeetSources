class Solution:
    def climbStairs(self, n: int) -> int:
        
        a,b = 0,1 #fibo approach, init a and b  

        for i in range(n):
            a,b = b, a+b # for each n a = b and b = the previous plus b
        return b
