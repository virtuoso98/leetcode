import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python Implements min heap by default.
        # Multiply entries by -1 for max heap
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)
        while len(stones) >= 2:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            diff = stone_1 - stone_2
            if diff != 0:
                heapq.heappush(stones, diff)
                
        # If Array not empty, multiply -1 to get +ve weight
        return 0 if len(stones) == 0 else -stones[0]