#include <iostream>
#include <vector>

using namespace std;

const int INF = 987654321, SWITCHES = 10, CLOCKS = 16;
const char linked[SWITCHES][CLOCKS+1] = {
    "xxx.............",
    "...x...x.x.x....",
    "xxx.x.....x...xx",
    "x...xxxx........",
    "......xxx.x.x...",
    "x.x...........xx",
    "...x..........xx",
    "...xx.x.......xx",
    ".xxxxx..........",
    "...xxx...x...x..",
};
// const int linked[SWITCHES][CLOCKS+1] = {{0, 1, 2},
//                                         {3, 7, 9, 11},
//                                         {4, 10, 14, 15},
//                                         {0, 4, 5, 6, 7},
//                                         {6, 7, 8, 10, 12},
//                                         {0, 2, 14, 15},
//                                         {3, 14, 15},
//                                         {4, 5, 7, 14, 15},
//                                         {1, 2, 3, 4, 5},
//                                         {3, 4, 5, 9, 13}};

bool istwelve(vector<int>& clocks) {
    for(int next = 0; next < clocks.size(); ++next) {
        if(clocks[next] != 12) 
            return false;
    }
    return true;
}

void push(vector<int>& clocks, int swtch) {
    for(int clock = 0; clock < CLOCKS; ++clock) {
        if(linked[swtch][clock] == 'x') {
            clocks[swtch] += 3;
            if(clocks[clock] == 15) clocks[clock] = 3;
        }
    }
}

int solve(vector<int>& clocks, int swtch) {
    if(swtch == SWITCHES)
        return istwelve(clocks) ? 0 : INF;
    
    int ret = INF;
    for (int cnt = 0; cnt < 4; ++cnt){
        ret = min(ret, cnt + solve(clocks, swtch + 1));
        push(clocks, swtch);
    }

    return ret;
}

int main(void) {
    int case_num = 0;
    cin >> case_num;

}