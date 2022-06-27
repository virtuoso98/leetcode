class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # No changes if pixel already in new colour:
        R, C = len(image), len(image[0])
        
        old_color = image[sr][sc]
        new_color = color
        if old_color == new_color:
            return image
        
        # Dfs, iterative
        stk = [(sr, sc)]
        
        while stk:
            r, c = stk.pop()
            if image[r][c] == old_color:
                image[r][c] = new_color
                if r - 1 >= 0: stk.append((r - 1, c))
                if r + 1 < R: stk.append((r + 1, c))
                if c - 1 >= 0: stk.append((r, c - 1))
                if c + 1 < C: stk.append((r, c + 1))
        
        return image