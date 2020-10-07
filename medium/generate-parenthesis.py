class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.res = []
        
        def generate (acc, left_count, right_count) :
            if left_count == n and right_count == n :
                self.res.append(acc)
                return
            
            if left_count < n : 
                generate (acc + "(", left_count + 1, right_count)
                
            
            if right_count < left_count :
                generate (acc + ")", left_count, right_count+ 1)
                
        generate("", 0, 0)
            
        return self.res 