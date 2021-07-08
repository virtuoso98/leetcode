class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq_table = {}
        for i in nums2:
            if i not in freq_table:
                freq_table[i] = 1
            else: 
                freq_table[i] += 1
                
        out = []
        for j in nums1:
            if j in freq_table and freq_table[j] > 0:
                out.append(j)
                freq_table[j] -= 1
                
        return out