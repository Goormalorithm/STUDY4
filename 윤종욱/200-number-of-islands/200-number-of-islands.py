class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # visited = set()
        
        def search(x,y):
            
            if len(grid)>x>=0 and len(grid[0])>y>=0 and (x,y) and grid[x][y]=='1':
                # visited.add((x,y))
                grid[x][y] = '3'
                
                search(x+1,y)
                search(x-1,y)
                search(x,y+1)
                search(x,y-1)
           
        islands = 0    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    search(i,j)
                    islands += 1
                        
        return islands