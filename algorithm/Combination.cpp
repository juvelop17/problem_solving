#include <iostream>

using namespace std;


void swap(int *a, int *b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void print_arr(int arr[], int r){
    for(int i=0;i<r;i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}

int arr[5] = {1,2,3,4,5};
bool visited[5];
int result[5];

// 재귀를 이용한 구현
void combination_1(int n, int r, int idx, int depth){
    if (depth == r) {
        print_arr(result, r);
        return;
    }

    for (int i=idx;i<n;i++){
        if (visited[i] == true) continue;
        visited[i] = true;
        result[depth] = arr[i];
        combination_1(n,r,i,depth+1);
        visited[i] = false;
    }
}

// 중복조합
void combination_repetition(int n, int r, int idx, int depth) {
    if (depth == r) {
        print_arr(result, r);
        return;
    }

    for (int i=idx;i<n;i++){
        result[depth] = arr[i];
        combination_repetition(n,r,i,depth+1);
    }
}

int main(){
    // combination_1(5,3,0,0);
    combination_repetition(5,3,0,0);
}


