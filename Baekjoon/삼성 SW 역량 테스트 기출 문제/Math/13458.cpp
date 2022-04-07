#include <iostream>
#include <cmath>

#define MAX 1000001
using namespace std;
int main(void) {
    int N = 0, B = 0, C = 0;
    int A[MAX] = {0,};

    cin >> N;
    for(int i = 0; i < N; i++){
        cin >> A[i];
    }
    cin >> B >> C;

    long long sum = 0;
    for(int i = 0; i < N; i++) {
        int man = A[i] - B;
        if(man > 0)
            sum += (long long)ceil((float)man/C);
    }
    cout << sum + N << endl;
    return 0;
}


/*
int main(void) {
    int N = 0, B = 0, C = 0;
    
    cin >> N;

    vector<int> A;
    for(int i = 0; i < N; ++i){
        int man = 0;
        cin >> man;
        A.push_back(man);
    }
    
    cin >> B >> C;
    
    long long sum = 0;
    
    for(vector<int>::iterator iter = A.begin(); iter != A.end(); ++iter){
        int temp = *iter-B;
        if(temp > 0)
            sum += ceil((float)temp/C);
    }
    cout << sum + N << endl;
    return 0;
}
*/