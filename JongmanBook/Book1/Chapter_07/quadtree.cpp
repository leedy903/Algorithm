/*
 * Question ID: QUADTREE
 * Level: Easy
 */

#include <iostream>
#include <string>

using namespace std;

#define MAX_SIZE 987654321

/*
char decompressed[MAX_SIZE][MAX_SIZE];

void decompress(string::iterator& it, int y, int x, int size){
    char head = *(it++);
    if(head     == 'b' || head == 'w') {
        for(int dy = 0; dy < size; ++dy) {
            for(int dx = 0; dx < size; ++dx) {
                decompressed[y+dy][x+dx] = head;
            }
        }
    }
    else {
        int half = size/2;
        decompress(it, y, x, half);
        decompress(it, y, x+half, half);
        decompress(it, y+half, x, half);
        decompress(it, y+half, x + half, half);
    }
}
*/
string reverse(string::iterator& it) {
    char head = *it;
    ++it;
    if(head == 'w' || head == 'b')
        return string(1, head);
    string upperLeft = reverse(it);
    string upperRight = reverse(it);
    string lowerLeft = reverse(it);
    string lowerRight = reverse(it);

    return string("x") + lowerLeft + lowerRight + upperLeft + upperRight;
}

int main(void) {
    int caseNum = 0;
    string decomporessed;
    cin >> caseNum;
    for(int i = 0; i < caseNum; ++i) {
        cin >> decomporessed;
        string::iterator it = decomporessed.begin();
        cout << reverse(it) << endl;
    }
    return 0;
}