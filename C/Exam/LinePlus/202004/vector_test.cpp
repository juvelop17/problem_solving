#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> vec(5);

    vec[0] = 1;
    cout << vec[0] << endl;

    vec[10] = 5;
    cout << vec[10] << endl;

    vec.at(10) = 10;
    cout << vec[10] << endl; 

    vector<int> vec2(5,2);
    cout << vec2[0] << endl;

    vector<vector<int> > vecvec;
    vecvec.resize(1);
    vecvec[0].push_back(1234);
    cout << vecvec[0].front() << endl;
}


