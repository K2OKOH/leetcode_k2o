/*
 * @lc app=leetcode.cn id=28 lang=cpp
 *
 * [28] 实现 strStr()
 */
# include<string>
# include<iostream>

using namespace std;
// @lc code=start
class Solution {
public:
    void GetNext(string needle)
    {
        int n_l = needle.size();
        for(int i=0;i<=n_l;i++)
        {
            
        }
    }
    int strStr(string haystack, string needle) {
        int h_l = haystack.size(), n_l = needle.size(), cnt = 0, pos = 0, ans = -1;
        if(n_l == 0)
        {
            return 0;
        }
        for(int i=0;i<=h_l-n_l;i++)
        {
            for(int j=0;j<n_l;j++)
            {
                if(haystack[i+j] == needle[j])
                {
                    if(j==0)
                    {
                        pos = i;
                    }
                    cnt++;
                    // cout << cnt << ": " << haystack[i+j] << "\n";
                }
                else
                {
                    // if(j>=2)
                    // {
                    //     i += (j-+1);
                    // }
                    cnt = 0;
                    // cout << "break" << "\n";
                    break;
                }
                if(cnt == n_l && ans == -1)
                {
                    ans = pos;
                }
            }
        }
        return ans;
    }
};
// @lc code=end

