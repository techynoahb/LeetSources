class Solution:
    def fib(self, n: int) -> int:
        x, z = 0, 1
        if n == 0:
            return 0
        for i in range(1,n):
            x, z = z, x + z
        return z
