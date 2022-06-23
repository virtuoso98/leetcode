class Solution:
    def isInOrder(self, word1, word2, idx_map) -> bool:
        # Traverse up to the minimum length of both words
        for i in range(min(len(word1), len(word2))):
            # Evaluate Cases where character order is different
            if idx_map[word1[i]] < idx_map[word2[i]]:
                return True
            elif idx_map[word2[i]] < idx_map[word1[i]]:
                return False
        
        # In order if word1 equal or shorter length than word2
        return len(word1) <= len(word2)
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx_map = dict()
        # Get word map order
        for i, c in enumerate(order):
            idx_map[c] = i
            
        for i in range(len(words) - 1):
            if not self.isInOrder(words[i], words[i + 1], idx_map):
                return False
        
        return True