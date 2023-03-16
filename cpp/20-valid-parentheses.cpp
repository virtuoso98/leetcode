class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> stk;
        map<char, char> char_map = {
            {'(', ')'},
            {'{', '}'},
            {'[', ']'}};

        for (auto &ch : s)
        {
            if (char_map.count(ch))
                stk.push(ch);
            else if (stk.empty())
                return false;
            else
            {
                char comp = stk.top();
                stk.pop();
                if (char_map[comp] != ch)
                    return false;
            }
        }

        return stk.empty();
    }
};