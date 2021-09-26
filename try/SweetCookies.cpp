# include <iostream>
# include <vector>
# include <algorithm>

using namespace std;

float find_p(vector<int> sw, int n, int k) {
    int time = n-k+1;
    float ans, temp;
    vector<int> sw_t = sw;
    float mix = 0;
    for(int i=0;i<time;i++) {
        sw_t = sw;
        for(int j=0;j<k;j++) {
            mix += sw[i+j];
            sw_t.erase(sw_t.begin()+i);
        }
        mix /= k;
        sw_t.push_back(mix);
        temp = sw_t[max_element(sw_t.begin(),sw_t.end())-sw_t.begin()] - sw_t[min_element(sw_t.begin(),sw_t.end())-sw_t.begin()];
        ans = min(ans ,temp);
        cout << ans << endl;
    }
    return ans;
}

int main() {
    vector<int> sw = {2,3,1,3};
    int n = 4, k = 2;
    float ans = 0;
    ans = find_p(sw, n, k);
    cout << ans << endl;
}