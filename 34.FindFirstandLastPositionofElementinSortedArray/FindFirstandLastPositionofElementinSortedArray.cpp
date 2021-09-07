# include<vector>
# include<iostream>
# include<algorithm>
# include<string>

using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int idx_f = 0, idx_l = nums.size()-1;
        vector<int> ans;
        if(idx_l < 0) return {-1, -1};
        while(idx_f < nums.size() && nums[idx_f++] != target);
        if(idx_f == nums.size() && nums[idx_f-1] != target) return {-1, -1};
        ans.push_back(idx_f-1);
        while(idx_l >= 0 && nums[idx_l--] != target);
        ans.push_back(idx_l+1);
        return ans;
    }
};

int main()
{
    Solution So;
    vector<int> nums = {1}, ans;
    int target = 1;

    ans = So.searchRange(nums, target);

    cout << "Out: [" << ans[0] << ", " << ans[1] << "]\n";
    return 0;
}
