class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if len(s) == 0:
            return 0

        if k > len(s):
            return len(s)

        window_chars = {}
        l = 0
        r = 0
        top_freq = 0
        max_seq_len = 0
        
        while r < len(s):
            if s[r] in window_chars:
                window_chars[s[r]] += 1
            else:
                window_chars[s[r]] = 1
                
            top_freq = max(top_freq, window_chars[s[r]])

            while (r - l + 1) - top_freq > k:
                window_chars[s[l]] -= 1
                l += 1

            max_seq_len = max((r - l + 1), max_seq_len)
            r += 1

        return max_seq_len

         