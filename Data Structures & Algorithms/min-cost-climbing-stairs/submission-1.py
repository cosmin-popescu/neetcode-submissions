class Solution:
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     # memiozation / cache previously calculated results
    #     n = len(cost)
    #     cache = [-1] * n

    #     def dfs(i):
    #         # we reached n 
    #         if i >= n:
    #             return 0
    #         # we already been at this step
    #         elif cache[i] != -1:
    #             return cache[i] 
    #         else:
    #             # update cost and pick minimum future path
    #             cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
    #             return cache[i]

    #     return min(dfs(0), dfs(1))

    #bottom up approach On time On space
    # def minCostClimbingStairs(self, cost: List[int]) -> int:

    #     n = len(cost)
    #     # cost to reach i
    #     dp = [0] * (n + 1)

    #     # to reach step i you must come from i-1 or i-2
    #     # after paying the cost[i-1] or cost[i-2]

    #     for i in range(2, n + 1):
    #         dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

    #     return dp[n]

    # bottom up with On time and O1 space
    # Use cost to keep track of costs
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        for i in range(n - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])