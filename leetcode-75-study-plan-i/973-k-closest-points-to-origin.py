class Solution:
    def calcDistance(self, point):
        return (point[1] ** 2 + point[0] ** 2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sorted_points = sorted(points, key = lambda point: self.calcDistance(point))
        return sorted_points[:k]