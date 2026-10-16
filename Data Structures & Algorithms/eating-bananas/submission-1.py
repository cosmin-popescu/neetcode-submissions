class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # just got this from Claude in a mock interview lmao

        # algo goes like:
        # we have h hours available to eat all the piles of baninos
        # have to find the k bananas per hour rate to eat.

        # deductions:
        # k is at most the biggest sized pile (meaning one pile per hour)
        # we have an average number of bananas that we need to eat 
        # in order to finish the pile so basically k is somehwere between
        # that average number and max pile

        # How to solve:
        # binary search in that interval [avg - max pile]
        # find a k and test for that k (this takes O(n) everytime)

        #find max and average
        # max_p = piles[0]
        # average_p = 0
        # for p in piles:
        #     average_p += p
        #     max_p = max(max_p, p)
        # average_p //= h

        left = -(-sum(piles) // h)
        right = max(piles)
        best_k = right

        # our k is in the interval [average_p, max_p]
        # now we binary search for it.

        while left <= right:

            potential_k = (left + right) // 2

            # check candidate
            hours_gone = 0
            for p in piles:
                hours_gone += -(-p // potential_k)
            
            # we fit, try to find smaller
            if hours_gone <= h:
                best_k = potential_k
                right = potential_k - 1
            # don't fit, go higher
            elif hours_gone > h:
                left = potential_k + 1

        return best_k

            