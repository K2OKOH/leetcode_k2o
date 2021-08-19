/*
 * @lc app=leetcode.cn id=39 lang=cpp
 *
 * [39] 组合总和
 */
# include<vector>
# include<iostream>
# include<algorithm>

using namespace std;
// @lc code=start
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target)
    {
        vector<vector<int>> ans;
        int now_pos = 0, n_sum = 0;
        sort(candidates.begin(),candidates.end());
        FindNext(now_pos, n_sum, target, ans, candidates);

        return ans;
    }
private:
    vector<int> ans_s;
    void FindNext(int now_pos, int n_sum, int target, vector<vector<int>>& ans, vector<int>& candidates)
    {
        int testval = n_sum + candidates[now_pos];
        for(int i = now_pos;i<candidates.size();i++)
        {
            testval = n_sum + candidates[i];
            for(int j=0;j<ans_s.size();j++)
            {
                // cout << ans_s[j] << ",";
            }
            // cout << "\n" << testval << " <-- " << candidates[i] << "\n";
            if(testval < target)
            {
                // cout << "push\n";
                ans_s.push_back(candidates[i]);
                FindNext(now_pos++, testval, target, ans, candidates);
                // cout << "return:" << testval << " , " << n_sum << "\n";
                testval = n_sum;
                ans_s.pop_back();
                // cout << "pop\n";
            }
            else if(testval == target)
            {
                // cout << "==\n";
                ans_s.push_back(candidates[i]);
                ans.push_back(ans_s);
                ans_s.pop_back();
                return;
            }
            else if(testval > target)
            {
                break;
            }
        }
    }
};
// @lc code=end

