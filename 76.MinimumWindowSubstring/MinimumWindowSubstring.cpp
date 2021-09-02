# include<vector>
# include<iostream>
# include<algorithm>
# include<string>

using namespace std;

class Solution {
public:
    string minWindow(string s, string t)
    {
        vector<int> chars(128,0);
        vector<bool> flag(128,false);
        // 统计 T中 字母是否存在 和 个数
        for(int i=0;i<t.size();i++)
        {
            flag[t[i]] = true;
            chars[t[i]]++;
        }

        int idx_l = 0, cnt = 0, min_size = s.size() + 1, min_l = 0;
        for(int idx_r=0;idx_r<s.size();idx_r++)
        {
            if(flag[s[idx_r]])
            {
                // chars 减成负数的时(s 中的该字符比 t中多了) cnt 不变
                if(--chars[s[idx_r]] >= 0)
                {
                    cnt++;
                }
            }
            // 如果已经全部找到
            while(cnt == t.size())
            {
                // 开始缩小 左 指针
                // 如果是最小字符串，就记录
                if(idx_r - idx_l < min_size)
                {
                    min_l = idx_l;
                    min_size = idx_r - idx_l + 1;
                }
                // 左指针指向 t 包含的字母
                if(flag[s[idx_l]] == true && ++chars[s[idx_l]] > 0)
                {
                    // t 已经不饱和了
                    cnt--;
                }
                idx_l++;
            }
        }
        
        return min_size > s.size()? "" : s.substr(min_l,min_size);
    }
};

int main()
{
    Solution So;
    string S = "ADOBECODEBANC" , T = "ABC";
    string ans;
    int m = 0, n = 1;
    ans = So.minWindow(S,T);

    cout << "Out: " << ans << "\n";
    return 0;
}
