/*
 * @lc app=leetcode.cn id=35 lang=cpp
 *
 * [35] 搜索插入位置
 */
#include <vector>
#include <iostream>

using namespace std;
// @lc code=start
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int nums_l = nums.size();
        int ans;
        int min_idx = 0, max_idx = nums_l-1, mid_idx;
        ans = nums_l;
        while(min_idx<=max_idx)
        {
            mid_idx = (min_idx + max_idx)/2;
            // cout << min_idx << '|' << mid_idx << '|' << max_idx << "\n";
            if(target<=nums[mid_idx])
            {
                ans = mid_idx;
                max_idx = mid_idx-1;
            }
            else if(target>nums[mid_idx])
            {
                min_idx = mid_idx+1;
            }
        }
        return ans;
    }
};
// @lc code=end

