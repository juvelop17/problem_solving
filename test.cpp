#include <iostream>

using namespace std;

typedef struct {
    int data1, data2;
} dataset;




int main(){
    dataset d1 = {1,2};
    dataset d2; 
    d2 = d1;
    cout << d2.data1 << " " << d2.data2 << endl; 
    d1.data1 = 10;
    cout << d1.data1 << " " << d1.data2 << endl; 
    cout << d2.data1 << " " << d2.data2 << endl; 

    return 0;
}






