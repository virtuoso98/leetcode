class Solution
{
public:
    vector<vector<int>> generate(int numRows)
    {
        vector<vector<int>> output = {{1}};
        for (int i = 1; i < numRows; i++)
        {
            vector<int> level = {};
            for (int j = 0; j <= i; j++)
            {
                if (j == 0)
                    level.push_back(output[i - 1][0]);
                else if (j == i)
                    level.push_back(output[i - 1][j - 1]);
                else
                    level.push_back(
                        output[i - 1][j - 1] + output[i - 1][j]);
            }
            output.push_back(level);
        }
        return output;
    }
};