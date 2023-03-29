class Solution
{
public:
    vector<int> sortedSquares(vector<int> &nums)
    {
        int i = 0;
        int j = nums.size() - 1;
        int k = nums.size() - 1;
        vector<int> output(nums.size());

        while (k >= 0)
        {
            if (abs(nums[i]) < abs(nums[j]))
            {
                output[k] = nums[j] * nums[j];
                k--;
                j--;
            }
            else
            {
                output[k] = nums[i] * nums[i];
                k--;
                i++;
            }
        }
        // reverse(output.begin(), output.end());
        return output;
    }
};