/*
 * @lc app=leetcode.cn id=20 lang=cpp
 *
 * [20] 有效的括号
 */
# include<iostream>
# include<string>

using namespace std;
// @lc code=start
class Solution {
public:
    bool isValid(string s) {
        int s_len = 0;
        string sta;
        s_len = s.size() - 1;
        for(int i=0;i<=s_len;i++)
        {
            if(s[i] == '(' || s[i] == '[' || s[i] == '{')
            {
                sta.push_back(s[i]);
            }
            else if(sta.length() <= 0)
            {
                return false;
            }
            else if(s[i] == ')')
            {
                if(sta[sta.length()-1] == '(')
                    sta.pop_back();
                else
                    return false;
            }
            else if(s[i] == ']')
            {
                if(sta[sta.length()-1] == '[')
                    sta.pop_back();
                else
                    return false;
            }
            else if(s[i] == '}')
            {
                if(sta[sta.length()-1] == '{')
                    sta.pop_back();
                else
                    return false;
            }
        }
        if(sta.length() != 0)
            return false;
        return true;
    }
};
// @lc code=end

