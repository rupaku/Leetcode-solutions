class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*n]*m
        dp[0][0]=grid[0][0]
        for i in range(m):
            if i > 0:
                dp[i][0]=dp[i-1][0] + grid[i][0]
            for j in range(1,n):
                if i== 0 and j > 0:
                    dp[i][j]=dp[i][j-1]+grid[i][j]
                else:
                    dp[i][j]=min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        return dp[m-1][n-1]