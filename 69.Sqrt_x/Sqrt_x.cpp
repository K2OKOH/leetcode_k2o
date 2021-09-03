# include<vector>
# include<iostream>
# include<algorithm>
# include<string>

using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        long long lookup = x, r = x, l = 0;
        if(x == 1)
        {
            return 1;
        }
        while(1)
        {
            lookup = (r + l)/2;
            cout << "lookup: " << lookup << "\n";
            if(lookup*lookup > x)
            {
                r = lookup;
            }
            else if(lookup*lookup < x)
            {
                l = lookup;
            }
            else
            {
                return lookup;
            }
            if(r-l == 1)
            {
                break;
            }
        }
        return l;
    }
};

int main()
{
    Solution So;
    int input = 2147395599, ans = 0;
    ans = So.mySqrt(input);

    cout << "Out: " << ans << "\n";
    return 0;
}
