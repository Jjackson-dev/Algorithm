class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        Input: grid = [
                      ["1","1","1","1","0"],
                      ["1","1","0","1","0"],
                      ["1","1","0","0","0"],
                      ["0","0","0","0","0"]
                    ]
                Output: 1
        """
        if not grid :
            return 0
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.discovered = []
        
        count = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if [i,j] in self.discovered:
                    continue
                
                if self.grid[i][j] == "1":
                    count +=1
                    self.dfs(i,j)
        return count
        #dfs
        
    def dfs(self,row, col):

        #위치에서 벗어나면 out
        if (row < 0) or (row >= self.rows):
            return False
        if (col <0) or (col >= self.cols):
            return 
        if [row,col] in self.discovered:
            return
        #위치 추가 
        self.discovered.append([row,col])
  
        if self.grid[row][col] == "1":
            #동서남북
            self.dfs(row+1, col)
            self.dfs(row-1, col)
            self.dfs(row, col+1)
            self.dfs(row, col-1)
