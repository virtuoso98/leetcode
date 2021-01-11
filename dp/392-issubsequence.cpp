class Solution {
public:
    bool isSubsequence(string s, string t) {
        int base_index = 0;
        int sl = s.length();
        int tl = t.length();
        int traverse = 0;
        
        while (traverse < tl) {
            if (base_index == sl) {
                break;
            } else {
                if (s[base_index] == t[traverse]){
                    base_index += 1;
                }
                traverse += 1;
            }   
        }
        return base_index == sl;         
    }
};