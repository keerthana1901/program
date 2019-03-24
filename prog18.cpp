#include<bits/stdc++.h>
using namespace std;

int main(void){
    int n1, m1, temp1, max_count=0;
    cin>>n1>>m1;

    vector<vector<int>> count(n1+1, vector<int>(m1+1));
    for(int i=0; i<n1; i++){
        for(int j=0; j<m1; j++){
            cin>>temp1;
            if(i==0 || j==0 || temp1 == 0){
                count[i+1][j+1] = temp1;
            } else {
                count[i+1][j+1] = 1 + min({count[i][j+1] , count[i+1][j], count[i][j]});
            }
            max_count = max(max_count, count[i+1][j+1]);
        }
    }
    for(int i=0; i<max_count; i++){
        for(int j=0; j<max_count; j++){
            cout<<1<<" ";
        }
        cout<<endl;
    }
    return 0;
}
