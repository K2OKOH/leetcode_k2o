# include<vector>
# include<iostream>
# include<algorithm>

using namespace std;

class Solution {
private:
    static bool VectorComFirst(vector<int> a, vector<int> b) {return(a[1]<b[1]);}

public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals)
    {
        int cnt = 0;
        sort(intervals.begin(),intervals.end(),[](const auto& u, const auto& v) {return u[1] < v[1];} );
        int num = intervals.size();
        int now_right = intervals[0][1];
        for(int i=1;i<num;i++)
        {
            if(now_right>intervals[i][0])
            {
                cnt++;
            }
            else
            {
                now_right = intervals[i][1];
            }
        }
        return cnt;
    }
};

int main()
{
    Solution S;
    vector<vector<int>> intervals={{1,2},{1,2},{1,2}};
    int ans = 0;
    ans = S.eraseOverlapIntervals(intervals);
    cout << "Out: " << ans << "\n";
    return ans;
}