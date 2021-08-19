/*
 * @lc app=leetcode.cn id=17 lang=cpp
 *
 * [17] 电话号码的字母组合
 */

// @lc code=start
# include <string>
# include <vector>
# include <algorithm>
# include <iostream>

using namespace std;
class Solution {
public:
    int ap(int deepth, string digits, string words)
    {
        // cout << "deepth = " << deepth << '\n';
        // 如果已经是叶节点
        if(deepth >= dig_n)
        {
            ans.push_back(words);
            // cout << "str:" << words << '\n';
        }
        else    // 还不是叶子节点
        {
            for(int w_i=0;w_i<letter[int(digits[deepth]-50)].size();w_i++)
            {
                // cout << "w_i: " << w_i << "\n";
                words[deepth] = letter[int(digits[deepth]-50)][w_i];
                // cout << "str:" << words << '\n';
                // cout << "<-" << letter[deepth][w_i] << "\n";
                deepth++;
                // cout << "deepth++ = " << deepth << '\n';
                ap(deepth, digits, words);
                deepth--;   // 退一格
                // cout << "deepth-- = " << deepth << '\n';
            }
        }
        return 0;
    }

    vector<string> letterCombinations(string digits) {
        dig_n = digits.size();
        string words(dig_n,'_');
        int dig_i = 0;
        ap(0, digits, words);
        if(ans.size()<=1)
        {
            return {};
        }
        return ans;
    }

private:
    vector<string> ans;
    int dig_n = 0;
    vector<string> letter = {"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
};
// @lc code=end

