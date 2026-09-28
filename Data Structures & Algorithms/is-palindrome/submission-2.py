class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s) < 1:
            return True

        curated = ''

        for c in s:
            if c.isalnum():
                curated += c.lower()

        start = 0
        end = len(curated) - 1

        while start < end:
            if curated[start].lower() != curated[end].lower():
                return False
            start += 1
            end -= 1
        return True
