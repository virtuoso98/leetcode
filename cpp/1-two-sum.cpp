class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        map<int, int> store;

        for (int i = 0; i < nums.size(); i++)
        {
            int comp = target - nums[i];
            if (store.count(comp))
                return {store[comp], i};
            else
                store[nums[i]] = i;
        }

        return {};
    }
};