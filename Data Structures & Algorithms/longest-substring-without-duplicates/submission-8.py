class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if len(s) == 0:
    #         return 0

    #     slow = 0
    #     fast = 0
    #     already_found = set()
    #     max_len = 0

    #     while fast < len(s):
    #         if s[fast] not in already_found:
    #             already_found.add(s[fast])
    #             fast += 1
    #             max_len = max(max_len, fast - slow)
    #         else:
    #             if s[slow] in already_found:
    #                 already_found.remove(s[slow])
    #             slow += 1

    #     return max_len

    # optimized        
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) < 2:
            return len(s)

        mapindex = {}
        slow = 0
        fast = 0
        max_len = 0

        while fast < len(s):
            if s[fast] in mapindex:
                 slow = max(mapindex[s[fast]] + 1, slow)
            mapindex[s[fast]] = fast
            max_len = max(max_len, fast - slow + 1)
            fast += 1

        return max_len

            

