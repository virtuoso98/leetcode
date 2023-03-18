class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int curr = 0;
        int lowest = INT_MAX;
        for (int price : prices)
        {
            lowest = min(lowest, price);
            curr = max(curr, price - lowest);
        }

        return curr;
    }
};