/*
 * @lc app=leetcode.cn id=18 lang=cpp
 *
 * [18] 四数之和
 */

// @lc code=start
# include <iostream>
# include <vector>
# include <algorithm>

using namespace std;
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int nums_n = 0;
        int a,b,c,d;
        long s = 0;
        vector<vector<int>> ans;
        sort(nums.begin(),nums.end());
        nums_n = nums.size();
        for(int a_i=0;a_i<nums_n-3;a_i++)
        {
            for(int b_i=a_i+1;b_i<nums_n-2;b_i++)
            {
                a = nums[a_i];
                b = nums[b_i];
                int c_i = 0, d_i = 0;
                c_i = b_i + 1;
                d_i = nums_n - 1;
                while(c_i<d_i)
                {
                    c = nums[c_i];
                    d = nums[d_i];
                    s = long(a)+long(b)+long(c)+long(d);
                    // cout << a_i << "," << b_i << "," << c_i << "," << d_i << "\n";
                    if(s>target)
                    {
                        d_i--;
                    }
                    else if(s<target)
                    {
                        c_i++;
                    }
                    else
                    {
                        ans.push_back({a,b,c,d});
                        // cout << " -> " << s << "\n";
                        while(nums[c_i]==nums[c_i+1] && c_i+1<d_i)
                        {
                            c_i++;
                        }
                        while(nums[d_i]==nums[d_i-1] && c_i<d_i-1)
                        {
                            d_i--;
                        }
                        d_i--;
                        c_i++;
                    }

                }
                while(nums[b_i]==nums[b_i+1] && b_i+1<nums_n-2)
                {
                    b_i++;
                    // cout << "b_i++" << "\n";
                }
            }
            while(nums[a_i]==nums[a_i+1] && a_i+1<nums_n-3)
            {
                a_i++;
                // cout << "a_i++" << "\n";
            }
        }
        return ans;
    }
};
// @lc code=end

