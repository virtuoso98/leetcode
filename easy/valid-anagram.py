class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def letter_count (string):
            dict = {}
            for i in string:
                if i in dict:
                    dict[i] += 1
                else:
                    dict[i] = 1
            return dict
        
        def check_equal (dict_1, dict_2):
            for keys in dict_1:
                
                if keys not in dict_2:
                    return False
                
                if (dict_1[keys] != dict_2[keys]):
                    return False
                
            return True
            
        dict_s = letter_count (s)
        dict_t = letter_count (t)
        
        return (check_equal(dict_s, dict_t) and check_equal(dict_t, dict_s))
