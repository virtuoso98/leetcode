class Solution:
    def countBitsByInt(self, n: int):
        n_bits = 0
        n_orig = n
        while n != 0:
            n_bits += 1 & n
            n >>= 1
        return (n_orig, n_bits)
    
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = list(map(self.countBitsByInt, arr))
        # Sort based on number of bits, then number
        arr = sorted(arr, key = lambda x: (x[1], x[0]))
        output = list(map(lambda x: x[0], arr))
        return output