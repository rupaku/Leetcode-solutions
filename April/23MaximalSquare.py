class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        max_square_len = 0
        dp = [[0] * (n + 1) for i in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (matrix[i - 1][j - 1] == '1'):
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    max_square_len = max(max_square_len, dp[i][j])
                    
        return max_square_len ** 2