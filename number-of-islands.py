class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
         
        def update (y, x) :
            if grid[y][x] == "0" :
                return
            else :
                grid[y][x] = "0"
            
                if y + 1 < height:
                    update(y + 1, x)
                if y - 1 >= 0:
                    update (y - 1, x)
                if x + 1 < length:
                    update (y, x + 1)
                if x - 1 >= 0:
                    update (y, x - 1)
        
        count = 0
        if len(grid) == 0:
            return 0 
        
        height = len(grid)
        length = len(grid[0])
        
        for x in range(length) :
            for y in range(height):
                
                if grid [y][x] == "1":
                    count += 1
                    update (y, x)
                    
        return count