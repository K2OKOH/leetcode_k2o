/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 三数之和
 */
# include<vector>
# include<algorithm>

// @lc code=start
using namespace std;
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        int num_n = 0, x = 0, y = 0, z = 0, s = 0;
        int x_i,y_i,z_i;
        num_n = nums.size();
        sort(nums.begin(),nums.end());
        // for(int i=0; i<num_n; i++){
        //     std::cout << nums[i] << ',';
        // }
        if(num_n < 3){
            return ans;
        }
        for(x_i=0; x_i<=num_n-2; x_i++){
            x = nums[x_i];
            // std::cout << x << '\n';
            if(x>0){
                break;
            }
            y_i = x_i + 1;
            z_i = num_n - 1;
            while(y_i < z_i){
                y = nums[y_i];
                z = nums[z_i];
                s = x+y+z;
                if(s == 0){
                    ans.push_back({x,y,z});
                    while(y_i<z_i && nums[y_i] == nums[y_i+1])
                        y_i++;
                    while(y_i<z_i && nums[z_i] == nums[z_i-1])
                        z_i--;
                    y_i++;
                    z_i--;
                }
                else if(s < 0){
                    y_i++;
                }
                else if(s > 0){
                    z_i--;
                }
            }
            while(x_i+1<num_n && nums[x_i] == nums[x_i+1])
                x_i++;
        }
        return ans;
    }
};
// @lc code=end

