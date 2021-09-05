#include <iostream>

using namespace std;


void quick_sort(int *data, int start, int end){
    if(start >= end){
        return;
    }

    int pivot = start;
    int i = pivot + 1;
    int j = end;
    int temp;

    while(i <= j){
        while(i <= end && data[i] <= data[pivot]){
            i++;
        }
        while(j > start && data[j] >= data[pivot]){
            j--;
        }

        if(i > j){
            temp = data[j];
            data[j] = data[pivot];
            data[pivot] = temp;
        } else {
            temp = data[i];
            data[i] = data[j];
            data[j] = temp;
        }
    }

    quick_sort(data, start, j-1);
    quick_sort(data, j+1, end);
}


int main(){
    int n = 10;
    int data[10] = {10,9,1,2,6,5,4,3,2,3};

    quick_sort(data,0,9);

    for(int i=0;i<n;i++){
        cout << data[i] << " ";
    }
    cout << endl;

    return 0;
}



