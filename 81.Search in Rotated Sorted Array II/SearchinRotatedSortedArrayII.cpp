# include<vector>
# include<iostream>
# include<algorithm>
# include<string>

using namespace std;

class Solution {
public:
    bool search(vector<int>& nums, int target)
    {
        int idx_l = 0, idx_r = nums.size()-1, idx_m = 0;
        while(idx_r >= idx_l)
        {
            idx_m = (idx_l + idx_r)/2;
            cout << idx_l << ": " << idx_m << ": " << idx_r << endl;
            // 如果 target 存在 就返回 true
            if(nums[idx_m] == target)
            {
                return true;
            }
            // 无法判断递增区间
            if(nums[idx_m] == nums[idx_l])
            {
                idx_l++;
            }
            // 刚开始默认 从小到大排序
            // 如果 l > mid : 那么反转点在左边，右边递增
            else if(nums[idx_m] <= nums[idx_l])
            {
                // target 在右边
                if(nums[idx_m] < target && target <= nums[idx_r])
                {
                    idx_l = idx_m + 1;
                }
                // traget 在左边
                else
                {
                    idx_r = idx_m - 1;
                }
            }
            // 如果 mid > r : 那么反转点在右边, 左边递增
            else
            {
                // target 在左边递增区间
                if(nums[idx_m] > target && nums[idx_l] <= target)
                {
                    idx_r = idx_m - 1;
                }
                else
                {
                    idx_l = idx_m + 1;
                }
            }
        }
        return false;
    }
};

int main()
{
    Solution So;
    vector<int> nums = {1,0,1,1,1};
    int target = 0;
    bool ans;
    ans = So.search(nums, target);
    cout << "Out: " << ans << "\n" << endl;
    return 0;
}
