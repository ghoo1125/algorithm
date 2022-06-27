from functools import lru_cache


class Solution:
    @lru_cache(maxsize=64)
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

if __name__ == '__main__':
    sol = Solution()
    print(sol.tribonacci(4))
    # t(4) -> t(3) + t(2) + t(1) 4misses
    # t(3) -> t(2) + t(1) + t(0) 2hits, 1miss
    # total 2hits 5misses
    print(sol.tribonacci.cache_info())