# include<vector>
# include<iostream>
# include<algorithm>
# include<numeric>
using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) 
    {
        int ans = 0, ratings_n = 0;
        ratings_n = ratings.size();
        vector<int> candy(ratings_n,1);
        for(int i=0;i<ratings_n-1;i++)
        {
            if(ratings[i] < ratings[i+1] && candy[i] >= candy[i+1])
            {
                candy[i+1] = candy[i]+1;
            }
        }
        for(int i=ratings_n-1;i>0;i--)
        {
            if(ratings[i] < ratings[i-1] && candy[i] >= candy[i-1])
            {
                candy[i-1] = candy[i]+1;
            }
        }
        ans = accumulate(candy.begin(),candy.end(),0);
        return ans;
    }
};

int main()
{
    Solution S;
    vector<int> ratings={1,3,2,2,1};
    int ans = 0;
    ans = S.candy(ratings);
    cout << "Out: " << ans << "\n";
    return ans;
}