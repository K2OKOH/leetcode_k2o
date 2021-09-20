# include<iostream>
# include<vector>

using namespace std;

int main()
{
    int A = 3, B = 3, C = 3, x = 1, y = 2, z = 3;
    int cost = -1;
    if(A == B && B == C) {
        if(y<=x && y<=z) {
            cost = y*2 + ((x<z)? x:z);
        }
    }
    else if(A>=B && B>=C) {
        int cos_a, cos_b;
        if(C > 1) {
            cos_b = (B-C+1)*y;
        }
        else{
            cos_b = -1;
        }
        if(B > 1) {
            if(B-1 == C) {
                if(C > 1)
                    cos_a = (A-C+1)*x;
                else
                    cos_a = -1;
            }
            else {
                cos_a = (A-B+1)*x;
            }
        }
        if(cos_a == -1) cost = cos_b;
        else if(cos_b == -1) cost = cos_a;
        else if(cos_b == -1 && cos_a == -1) cost = -1;
        else cost = (cos_a < cos_b)? cos_a : cos_b;
    }
    else if(A<=B && B<=C) {
        int cos_c, cos_b;
        if(A > 1) {
            cos_b = (B-A+1)*y;
        }
        else{
            cos_b = -1;
        }

        if(B > 1) {
            if(B-1 == A) {
                if(A > 1)
                    cos_c = (C-A+1)*z;
                else
                    cos_c = -1;
            }
            else {
                cos_c = (C-B+1)*z;
            }
        }
        if(cos_c == -1) cost = cos_b;
        else if(cos_b == -1) cost = cos_c;
        else if(cos_b == -1 && cos_c == -1) cost = -1;
        else cost = (cos_c < cos_b)? cos_c : cos_b;
    }
    else{
        cost = 0;
    }
    cout << cost << endl;
    return 0;
}