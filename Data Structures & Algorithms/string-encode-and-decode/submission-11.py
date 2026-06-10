class Solution:

    def encode(self, strs: List[str]) -> str:
        # if empty, return ""
        if not strs:
            return ""
        # we want to take the sizes of the strings, and append them with the strings.
        sizes, res = [], []
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res.append(str(sz))
            res.append(',')
        res.append('#')
        for s in strs:
            res.append(s)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j+1
        i += 1

        # s = 5,5#HelloWorld
        for size in sizes:
            res.append(s[i: i+size])
            i += size
        
        return res
        
