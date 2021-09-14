# include<vector>
# include<iostream>
# include<algorithm>
# include<string>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int ans = 0, temp = 0;
        // 排序两次 找出第k大的数
        for(int i=0;i<k;i++) {
            for(int j=0;j<nums.size()-i-1;j++) {
                if(nums[j] > nums[j+1]) {
                    // 交换顺序
                    temp = nums[j];
                    nums[j] = nums[j+1];
                    nums[j+1] = temp;
                }
            }
        }
        ans = nums[nums.size()-k];
        return ans;
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
