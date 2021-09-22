# include<vector>
# include<iostream>
# include<algorithm>
# include<string>

using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        // 从位置0开始搜索
        dfs(nums, ans, 0);
        return ans;
    }
private:
    void dfs(vector<int>& nums, vector<vector<int>>& ans, int idx) {
        // 判断是否到叶结点
        if(idx == nums.size()-1) {
            ans.push_back(nums);
            return;
        }
        for(int i=idx;i<nums.size();i++) {
            swap(nums[idx], nums[i]);
            dfs(nums,ans,idx+1);
            swap(nums[idx], nums[i]);
        }
    }
};

int main()
{
    Solution So;
    vector<int> nums = {1,2,3};
    vector<vector<int>> ans;
    ans = So.permute(nums);
    for(auto a : ans) {
        cout << "[";
        for(auto num : a) { cout << num << ",";}
        cout << "],";
    }
    return 0;
}
