#include <iostream>
#include <unordered_map>
using namespace std;


#define MAX_N 100000

unordered_map<string, int> um;


void hashInit() {
    // 해시테이블 사이즈 증가
    um.reserve(MAX_N);

    // 해시테이블 버킷 사이즈 증가
    float z = um.max_load_factor();
    um.max_load_factor ( z / 2.0 );

    um.clear();
}

void printMapInfo() {
    std::cout << "current max_load_factor: " << um.max_load_factor() << std::endl;
    std::cout << "current size: " << um.size() << std::endl;
    std::cout << "current bucket_count: " << um.bucket_count() << std::endl;
    std::cout << "current load_factor: " << um.load_factor() << std::endl;
    cout << endl;
}


int main(){

    if(um.empty()){
        cout<<"unordered_map은 비어있습니다"<<endl;
    }

    printMapInfo();
    hashInit();
    printMapInfo();
    um.clear();
    printMapInfo();




    char *str1 = "hello";
    um.insert(make_pair(str1, 1));
    printf("%s %d\n", str1, um.find(str1)->second);
    um.erase(str1);

    char *str2 = "hi";
    um[str2] = 2;
    printf("%s %d\n", str2, um[str2]);

    um["banana"]=2;
    printf("%s %d\n", "banana", um["banana"]);


    unordered_map<string, int*> newmap;
    printf("%s %d\n", "exam", um["exam"]);
    printf("%s %d\n", "exam", newmap["exam"]);


    um.insert({"melon",3});

    cout<<"unordered_map의 크기는 "<<um.size()<<" 입니다"<<endl;

    // auto로 해도 무방
    for(pair<string,int> elem : um){
        cout<<"key : "<<elem.first<<" value : "<<elem.second<<endl;
    }

    // find 대신 count로 확인 가능
    if(um.find("banana")!=um.end()){
        um.erase("banana");
    }

    cout<<"unordered_map의 크기는 "<<um.size()<<" 입니다"<<endl;
    for(auto elem : um){
        cout<<"key : "<<elem.first<<" value : "<<elem.second<<endl;
    }

    return 0;
}