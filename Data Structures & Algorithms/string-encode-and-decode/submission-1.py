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
        idx = 0

        while idx < len(s):
            c = s[idx]

            if c == '#':
                num = int(snum)
                if num == 0:
                    res.append('')
                else:
                    res.append(s[idx + 1 : idx + num + 1])
                idx += num + 1
                snum = ''
            else:
                snum += c
                idx += 1
        return res
