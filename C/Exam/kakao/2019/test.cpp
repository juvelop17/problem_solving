#include <iostream>

using namespace std;

string a,b;

int main(){
    a = "hello";
    b = a;
    cout << "a b : " << a << " " << b << endl;
    cout << "&a &b : " << &a << " " << &b << endl;
    a = "hi";
    cout << "a b : " << a << " " << b << endl;
    cout << "&a &b : " << &a << " " << &b << endl;


    return 0;
}


