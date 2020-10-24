#include <iostream>
#include <string>
#include <vector>

using namespace std;



void display(vector<int> vec){
    for(int i=0;i<vec.size();i++){
        cout << vec[i] << " ";
    }
    cout << endl;
}

vector<int> solution(vector<int> prices){
    vector<int> answer;


    answer = prices;
    return answer;
}

int main() {
    static const int arr[] = {5, 3, 7, 9, 5, 2, 4, 9, 10, 6};  
    vector<int> prices (arr, arr + sizeof(arr) / sizeof(arr[0]) );

    display(solution(prices));

    return 0;
}



