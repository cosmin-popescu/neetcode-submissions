class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # memiozation / cache previously calculated results
        n = len(cost)
        cache = [-1] * n

        def dfs(i):
            # we reached n 
            if i >= n:
                return 0
            # we already been at this step
            elif cache[i] != -1:
                return cache[i] 
            else:
                # update cost and pick minimum future path
                cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
                return cache[i]

        return min(dfs(0), dfs(1))