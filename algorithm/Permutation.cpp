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
void permutation_1(int n, int r, int depth) {
    if (depth == r){
        print_arr(arr, r);
        return;
    }

    for(int i=depth;i<n;i++){
        swap(&arr[i],&arr[depth]);
        permutation_1(n,r,depth+1);
        swap(&arr[i],&arr[depth]);
    }
}

// 재귀를 이용한 구현 2
void permutation_2(int n, int r, int depth){
    if (depth == r){
        print_arr(result, r);
        return;
    }

    for(int i=0;i<n;i++){
        if (visited[i] == true) continue;
        visited[i] = true;
        result[depth] = arr[i];
        permutation_2(n,r,depth+1);
        visited[i] = false;
    }
}

// 중복순열
void permutation_repetition(int n, int r, int depth){
    if (depth == r) {
        print_arr(result, r);
        return;
    }

    for(int i=0;i<n;i++){
        result[depth] = arr[i];
        permutation_repetition(n,r,depth+1);
    }
}

int main(){
    // permutation_1(5,3,0);
    // permutation_2(5,3,0);
    permutation_repetition(5,3,0);
}


