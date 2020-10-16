class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        empty_s = []
        for c in S:
            if c == '#':
                if empty_s:
                    empty_s.pop()
            else:
                empty_s.append(c)

        empty_t = []
        for c in T:
            if c == '#':
                if empty_t:
                    empty_t.pop()
            else:
                empty_t.append(c)

        return ''.join(empty_s) == ''.join(empty_t)