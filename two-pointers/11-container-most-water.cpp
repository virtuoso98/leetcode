class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;
        int ans = 0;
        int water;
        while (l < r){
            water = (r - l) * min(height[l], height[r]);
            ans = max(water, ans);
            if (height[l] < height[r]){
                l += 1;
            } else {
                r -= 1;
            }    
        }
        return ans;
    }
};