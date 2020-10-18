class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N-1:
            return -1
        trusted_by= [0]*(N+1)
        trust_i_have =[0]*(N+1)
        for a, b in trust:
            trust_i_have[a] += 1
            trusted_by[b] += 1
        for i in range(1,N+1):
            if trusted_by[i] == N-1 and trust_i_have[i] == 0:
                return i
        return -1
        