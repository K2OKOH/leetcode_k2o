# include<vector>
# include<iostream>
# include<algorithm>
# include<string>

using namespace std;

class Solution {
public:
    // 快速查找法
    int FindMid(vector<int>& nums, int l, int r) {
        int i = l + 1, j = r;
        while(1) {
            while(i<r && nums[i]<=nums[l]) {
                i++;
            }
            while(j>l && nums[j]>=nums[l]) {
                j--;
            }
            if(i>=j) {
                break;
            }
            swap(nums[i], nums[j]);
        }
        swap(nums[l], nums[j]);
        // for(int z = 0;z<nums.size();z++) {
        //     cout << nums[z] << ", ";
        // }
        // cout << endl;
        return j;
    }

    int findKthLargest(vector<int>& nums, int k) {
        int idx_l = 0, idx_r = nums.size()-1, mid = 0;
        k = nums.size() - k;
        while(idx_l < idx_r) {
            mid = FindMid(nums, idx_l, idx_r);
            // cout << mid << endl;
            if(mid == k) {
                return nums[mid];
            } else if(mid < k) {
                idx_l = mid + 1;
            } else if(mid > k) {
                idx_r = mid - 1;
            }
        }
        return nums[idx_l];
    }
};

int main()
{
    Solution So;
    vector<int> nums = {3,2,1,5,6,4};
    int target = 2, ans = 0;
    ans = So.findKthLargest(nums, target);
    cout << "Out: [" << ans << "]\n";
    return 0;
}
