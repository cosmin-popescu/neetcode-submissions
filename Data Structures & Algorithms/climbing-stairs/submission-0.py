class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n

        def dive(i):
            if i == n:
                return 1
            elif i > n:
                return 0
            elif cache[i] != -1:
                return cache[i]
            else:
                cache[i] = dive(i + 1) + dive(i + 2)
                return cache[i]

        return dive(0)
        