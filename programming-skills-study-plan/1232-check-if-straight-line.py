class Solution:
    def getGradient(self, p1, p2):
        if p2[0] == p1[0]:
            return float('inf')
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(2, len(coordinates)):
            p0 = coordinates[i]
            p1 = coordinates[i - 1]
            p2 = coordinates[i - 2]
            grad0 = self.getGradient(p0, p1)
            grad1 = self.getGradient(p1, p2)
            if not math.isclose(grad0, grad1):
                return False
        return True