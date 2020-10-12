class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        num_list = len(matrix)
        if num_list == 0 :
            return False
        list_length = len(matrix[0])
        if list_length == 0 :
            return False
        
        has_index = False
        
        for i in range(num_list):
            if matrix[i][0] <= target and target <= matrix[i][list_length - 1] :
                has_index = True
                store_index = i
                break 
        
        if not has_index :
            return False 
        
        for j in matrix[store_index]:
            if j == target:
                return True
        
        return False