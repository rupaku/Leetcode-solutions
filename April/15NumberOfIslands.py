class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        n=len(grid)
        m=len(grid[0])
        res=0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    res=res+1
                self.make_water(i,j,n,m,grid)
        return res
    
    def make_water(self,i,j,n,m,grid):
        if i < 0 or j < 0 or i >=n or j >= m:
            return
        if grid[i][j] == "0":
            return
        else:
            grid[i][j] = "0"
        self.make_water(i+1,j,n,m,grid)
        self.make_water(i,j+1,n,m,grid)
        self.make_water(i-1,j,n,m,grid)
        self.make_water(i,j-1,n,m,grid)
        
        
        