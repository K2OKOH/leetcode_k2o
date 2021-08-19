/*
 * @lc app=leetcode.cn id=27 lang=cpp
 *
 * [27] 移除元素
 */
# include<vector>
# include<iostream>

using namespace std;
// @lc code=start
class Solution {
public:
    int removeElement(vector<int>& nums, int val)
    {
        int n_l = nums.size(), cnt = 0;
        // cout << n_l << "\n";
        for(int i=0;i<n_l;i++)
        {
            if(nums[i-cnt]==val)
            {
                // cout << "erase: " << i << "\n";
                nums.erase(nums.begin()+i-cnt);
                cnt++;
            }
            else{
                // cout << "save: " << i << "\n";
            }
        }
        return nums.size();
    }
};
// @lc code=end

