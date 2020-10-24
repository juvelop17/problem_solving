#include <iostream>
#include <cstdio>

using namespace std;

int N,strike[100],ball[100];
char num[100][3];



bool check(int ans[]){
    bool isTrue = true;
    int cnt_s,cnt_b;
    for (int i=0;i<N;i++){
        cnt_s = cnt_b = 0;
        for (int j=0;j<3;j++){
            if (num[i][j] == ans[j]){
                cnt_s++;
            } else {
                for (int k=0;k<3;k++){
                    if (num[i][j] == ans[k]){
                        cnt_b++;
                    }
                }
            }
        }
        if (cnt_s != strike[i] || cnt_b != ball[i]){
            isTrue = false;
        }
    }
    return isTrue;
}


void swap(int *a, int *b){
    int *tmp;
    tmp = a;
    a = b;
    b = tmp;
}


void printArr(int arr[],int r){
    cout << "printArr : ";
    for(int i=0;i<r;i++){
        cout << arr[i];
    }
    cout << endl;
}


void perm(int arr[],int depth,int n, int r){
    if (depth == r){
        bool isTrue;
        int ans[3] = {arr[0],arr[1],arr[2]};
        isTrue = check(ans);
        if (isTrue == true){
            printArr(arr,r);
        }
        return;
    }

    for (int i=depth;i<n;i++){
        swap(arr[i],arr[depth]);
        perm(arr,depth+1,n,r);
        swap(arr[i],arr[depth]);
    }
}




int solution(){
    int arr[9] = {1,2,3,4,5,6,7,8,9};
    perm(arr,0,9,3);

    return 0;
}

int main(){
    ios::sync_with_stdio(0);
    freopen("input.txt","r",stdin);

    cin >> N;
    for(int i=0;i<N;i++){
        cin >> num[i][0] >> num[i][1] >> num[i][2] >> strike[i] >> ball[i];
    }

    solution();

    return 0;
}


