class Solution:
    def fib(self, n: int) -> int:
        if (n <= 1):
            return n
        else:
            return Solution().fib(n-1) + Solution().fib(n-2)
print(Solution().fib(10))