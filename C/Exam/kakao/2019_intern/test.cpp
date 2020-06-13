#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;




#include <cstring>


int main(){
    string s = "{{2},{2,1},{2,1,3},{2,1,3,4}}";
    // string s = "{{1,2,3},{2,1},{1,2,4,3},{2}}";
    // string s = "{{20,111},{111}}";
    // string s = "{{123}}";
    // string s = "{{4,2,3},{3},{2,3,4,1},{2,3}}";
    
    char ch[1000];
    strcpy(ch,s.c_str());
    cout << ch << endl;

    char *ptr = strtok(ch, "{");
    char *ptr2;

    while (ptr != NULL)
    {   
        *ptr2 = *ptr;
        while(ptr2)
        cout << ptr << endl;
        ptr = strtok(NULL, "{");
        ptr = strtok(NULL, ",");
    }
    

    return 0;
}




