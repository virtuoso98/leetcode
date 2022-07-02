class Solution:
    def createCount(self, t: str) -> dict:
        count = {}
        for c in t:
            if c not in count:
                count[c] = 0
            count[c] += 1
        return count
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        
        window = len(p)
        count_p = self.createCount(p)
        count_s = self.createCount(s[:window])        
        start_idx = []        
        
        for i in range(len(s) - window + 1):
            # No character replacement is required
            if i == 0:
                if count_s == count_p: start_idx.append(i)
            else:
                # Character to remove and add to count_s
                remove = s[i - 1]
                add = s[i + window - 1]
                
                # Add operation
                if add not in count_s:
                    count_s[add] = 1
                else:
                    count_s[add] += 1
                
                # delete operation. Delete so that dict can be compared
                count_s[remove] -= 1               
                if count_s[remove] == 0: 
                    del count_s[remove]
                
                if count_s == count_p: start_idx.append(i)    
                
        return start_idx