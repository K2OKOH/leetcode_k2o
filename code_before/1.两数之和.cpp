/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */

# include<vector>
# include<iostream>
# include<algorithm>

using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        int nums_n = 0;
        nums_n = nums.size();
        for(int x_i=0;x_i<nums_n;x_i++){
            for(int y_i=x_i+1;y_i<nums_n;y_i++){
                if(target==(nums[x_i] + nums[y_i])){
                    ans = {x_i,y_i};
                }
            }
        }
        return ans;
    }
};
// @lc code=end