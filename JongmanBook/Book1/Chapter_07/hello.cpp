#include <iostream>
#include <string>

using namespace std;

int main(void) {
    const char one[5] = {'a', 'b' , 'c', 'd', 'e'};
    //string two(5, 'w');
    string two(one); 
    //string::iterator it = two.begin();
    for (string::iterator it = two.begin(); it != two.end(); ++it){
        cout << *it << endl;
        if (*it == 'c') {
            // two.erase(2); THIS MAKES SEGMENTATION FAULT
        }
    }
    cout << two << endl;
    //cout << one << endl << two << endl;
    //cout << sizeof(one) << endl << two.size() << endl;
    return 0;
}