class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        char_count = {}
        for c in secret:
            if c not in char_count:
                char_count[c] = 1
            else:
                char_count[c] += 1
                
        n_bulls = 0
        n_cows = 0
        
        for i, c in enumerate(guess):
            # check for presence of character
            if c in char_count:
                if secret[i] == c:
                    n_bulls += 1
                    # reduce cow count because of this scenario:
                    # "secret: '111', guess: '011'
                    n_cows -= 1 if char_count[c] < 1 else 0
                else:
                    # increase cow count by 1 if chars still available
                    n_cows += 1 if char_count[c] >= 1 else 0
                char_count[c] -= 1
        
        
        return f"{n_bulls}A{n_cows}B"