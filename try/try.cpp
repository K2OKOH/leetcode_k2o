# include<iostream>
# include<vector>

using namespace std;

int main()
{
    int a = 1;
    vector<int> aa = {1,2,3};
    aa.push_back(a);
    a++;

    cout << "hello world\n"; 
    return 0;
}