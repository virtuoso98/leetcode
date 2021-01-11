class Solution:
    def numTeams(self, rating: List[int]) -> int:
        """
        Fix the middle, then find left and right and multiply
        Greedy algorithm that gets the job done
        """
        acc = 0 
        pointer = 1
        
        while pointer < len(rating) - 1 :
            leftdesc = 0
            rightdesc = 0 
            rightasc = 0 
            leftasc = 0 
            cache = rating[pointer]
            
            for i in range (pointer):
                if rating[i] < cache :
                    leftasc += 1
                if rating[i] > cache :
                    leftdesc += 1
            
            for j in range(pointer + 1, len(rating)):
                if cache < rating[j]:
                    rightasc += 1
                if cache > rating[j]:
                    rightdesc += 1
            
            acc += rightasc * leftasc + rightdesc * leftdesc
            pointer += 1
            
        return (acc)