class Solution:
    def getManhattanDist(self, x: int, y: int, i: int, j: int):
        return abs(x - i) + abs(y - j)
    
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = float('inf')
        final_idx = -1
        for idx, (i, j) in reversed(list(enumerate(points))):
            dist = self.getManhattanDist(x, y, i, j)
            if (i == x or j == y) and dist <= min_dist:
                min_dist = dist
                final_idx = idx  
        return final_idx