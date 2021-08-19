/*
 * @lc app=leetcode.cn id=40 lang=cpp
 *
 * [40] 组合总和 II
 */

# include<vector>
# include<iostream>
# include<algorithm>

using namespace std;
// @lc code=start
class Solution {
private:
    vector<vector<int>> ans;
    vector<int> ans_s;
    void FindNext(vector<int>& candidates, int target, int& testval, int NP, vector<bool>& used)
    {
        for(int i=NP;i<candidates.size();i++)
        {
            if (i > NP )
            {
                if(candidates[i] == candidates[i - 1])
                {
                    // cout << "contiune i:" << i << "\n";
                    continue;
                }
            }
            testval += candidates[i];
            // cout << "  i: " << i << " | ";
            // for(int j=0;j<ans_s.size();j++)
            // {
            //     cout << ans_s[j] << ",";
            // }
            // cout << " <-- " << candidates[i];
            // cout << "  sum: " << testval << "\n";
            ans_s.push_back(candidates[i]);
            // for(int j=0;j<used.size();j++)
            // {
            //     cout << used[j] << ",";
            // }
            // cout << " <-- used \n";
            if(testval < target && i<candidates.size())
            {
                used[i] = true;
                // cout << "FN\n";
                FindNext(candidates, target, testval, ++i, used);
                used[i] = false;
                i--;
                testval -= ans_s.back();
                ans_s.pop_back();
                // cout << "pop --> i: " << i << "\n";
                // testval -= ans_s.back();
                // ans_s.pop_back();
            }
            else if(testval == target)
            {
                ans.push_back(ans_s);
                testval -= ans_s.back();
                ans_s.pop_back();
                // cout << "==\n";
                return;
            }
            else if(testval > target)
            {
                testval -= ans_s.back();
                ans_s.pop_back();
                // cout << ">\n";
                return;
            }
        }
        return;
    }
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) 
    {
        int testval = 0;
        vector<bool> used(candidates.size(), false);
        sort(candidates.begin(),candidates.end());
        // cout << "start\n";
        FindNext(candidates, target, testval, 0, used);
        // cout << "la";
        // sort(ans.begin(),ans.end());
        // ans.erase(unique(ans.begin(), ans.end()), ans.end());
        return ans;
    }
};
// @lc code=end

