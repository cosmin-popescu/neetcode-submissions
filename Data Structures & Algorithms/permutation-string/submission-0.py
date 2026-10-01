class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        chars = [0] * 26

        # register s1 counts
        for c in s1:
            chars[ord(c) - ord('a')] += 1 

        start = 0
        end = 0
        chars2 = [0] * 26

        # window end reaches end of s2
        while end < len(s2):
            # register char in chars2
            idx = ord(s2[end]) - ord('a')
            chars2[idx] += 1
            
            # move window
            if (end - start + 1) > len(s1):
                idx = ord(s2[start]) - ord('a')
                chars2[idx] -= 1
                start += 1

            # check matches
            if chars2 == chars:
                return True
            
            end += 1

        return False

            
            
            
            

            
