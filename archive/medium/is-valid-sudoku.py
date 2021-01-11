class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        length = len(board)
        last_index = length - 1
        
        for i in range(length):
            self.cache3 = set()
            self.cache4 = set()
            for j in range(length):
                
                if board[j][i] in self.cache3 :
                    return False
                if board[j][i] != "." :
                    self.cache3.add(board[j][i])
                    
                if board[i][j] in self.cache4 :
                    return False
                if board[i][j] != "." :
                    self.cache4.add(board[i][j])
                
        for i in range (3):
            for j in range (3): 
                self.cache5 = set()
                for k in range (3):
                    for l in range (3):
                        if board[3 * i + k][3 * j + l] in self.cache5 :
                            return False
                        if board[3 * i + k][3 * j + l] != "." : 
                            self.cache5.add(board[3 * i + k][3 * j + l])
        
        return True