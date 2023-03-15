class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;

        int i = 1;
        int j = 2;

        for (int k = 0; k < n - 2; k++) {
            int tmp = i + j;
            i = j;
            j = tmp;
        }

        return j;
    }
};