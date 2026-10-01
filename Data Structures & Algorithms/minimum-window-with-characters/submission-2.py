class Solution:

    # # after debugging with Gemini, my original idea led to this
    # def minWindow(self, s: str, t: str) -> str:
    #     if len(t) > len(s):
    #         return ""

    #     res = ""

    #     # Frequency map for t
    #     freq_t = {} 
    #     for c in t:
    #         freq_t[c] = freq_t.get(c, 0) + 1
        
    #     # Iterate with a dynamic window size, starting with len(s) down to len(t)
    #     for wlen in range(len(s), len(t) - 1, -1):
            
    #         wstart = 0
    #         wend = wstart + wlen

    #         # Create char frequency for initial window setup
    #         freq_w = {}
    #         for c in s[wstart:wend]:
    #             freq_w[c] = freq_w.get(c, 0) + 1

    #         # Iterate across s with current window size
    #         while wend <= len(s): # Note: changed to <= to correctly evaluate the last character shift
    #             t_found = True

    #             # FIXED: Proper match checking
    #             for c in freq_t:
    #                 # If character is missing entirely or doesn't have enough count
    #                 if c not in freq_w or freq_w[c] < freq_t[c]:
    #                     t_found = False
    #                     break

    #             # If all conditions match, overwrite with the smaller window size               
    #             if t_found:
    #                 res = s[wstart:wend]
                
    #             # Advance the window safely:
    #             # 1. Remove left character
    #             if wstart < len(s):
    #                 freq_w[s[wstart]] -= 1
    #                 if freq_w[s[wstart]] == 0:
    #                     freq_w.pop(s[wstart])
    #             wstart += 1

    #             # 2. Add right character
    #             if wend < len(s):
    #                 freq_w[s[wend]] = freq_w.get(s[wend], 0) + 1
    #             wend += 1

    #     return res

    # #2 - 2 pointer approach
    def minWindow(self, s: str, t: str) -> str:

        res = ""

        if len(t) > len(s):
            return ""

        # build t frequency map
        freq_t = {}
        for c in t:
            freq_t[c] = freq_t.get(c, 0) + 1

        left = 0
        right = 0

        best_left = 0
        best_right = 0
        min_len = float("inf")

        freq_w = {}
        another_one = 0

        # advance right until t is inculded in window
        while right < len(s):
            # add right to freq map
            freq_w[s[right]] = freq_w.get(s[right], 0) + 1
            # check if freq map contains t
            # handles duplicates due to '=='
            if s[right] in freq_t and freq_t[s[right]] == freq_w[s[right]]:
                another_one += 1
            if another_one == len(freq_t):
                # advance left until t is not included anymore
                while another_one == len(freq_t) and left <= right:
                    # check if we have a new smaller substring
                    cur_len = right - left + 1
                    if cur_len < min_len:
                        min_len = cur_len
                        best_right = right
                        best_left = left
                    # remove from map
                    freq_w[s[left]] = freq_w.get(s[left], 0) - 1
                    # check if condition still satisfies
                    if s[left] in freq_t:
                        if freq_w[s[left]] < freq_t[s[left]]:
                            # no more t in window
                            another_one -= 1
                    left += 1

            right += 1

        # t not found
        if min_len == float("inf"):
            return ""

        # return slice of best found
        res = s[best_left:best_right + 1]
        return res