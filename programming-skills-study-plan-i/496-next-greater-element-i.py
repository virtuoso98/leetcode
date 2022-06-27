class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx_map = {}
        for i, v in enumerate(nums2):
            idx_map[v] = i
            
        output = []
        for v in nums1:
            i = idx_map[v] + 1
            is_element_found = False
            for j in range(i, len(nums2)):
                if v < nums2[j]:
                    is_element_found = True
                    output.append(nums2[j])
                    break
            if not is_element_found:
                output.append(-1)
        return output