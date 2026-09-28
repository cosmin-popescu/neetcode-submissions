class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            l = len(s)
            res += str(l) + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        snum = ''
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            # advance past #
            i = j + 1

            res.append(s[i : i+length])
            
            # advance with legnth characters that were extracted
            i += length
        return res
