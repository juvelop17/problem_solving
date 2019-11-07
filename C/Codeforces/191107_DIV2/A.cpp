#include <iostream>
#include <cstdio>

using namespace std;

int k,n,a[1000];



void QuickSort(int arr[], int left, int right)
{
    int L = left, R = right;
    int temp;
    int pivot = arr[(left + right) / 2]; 

    while (L < R) {
        while (arr[L] < pivot) L++;
        while (arr[R] > pivot) R--;

        if (L <= R) {
            if (L < R) {
                temp = arr[L];
                arr[L] = arr[R];
                arr[R] = temp;
            }
            L++; R--; 
        }
    }
    if (left < R) QuickSort(arr, left, R);
    if (right > L) QuickSort(arr, L, right);
}


int solution(){
    int max_height,height,index,cnt;
    cnt = 0;
    index = n-1;
    while (index >= 0) {
        height = a[index];
        if (cnt + 1 > height){
            break;
        }
        cnt++;
        index--;
    }

    return cnt;
}


int main(){
    // freopen("input.txt","r",stdin);

    cin >> k;
    for(int i=0;i<k;i++){
        cin >> n;
        for (int j=0;j<n;j++){
            cin >> a[j];
        }
        QuickSort(a,0,n-1);
        cout << solution() << endl;
    }

    return 0;
}


