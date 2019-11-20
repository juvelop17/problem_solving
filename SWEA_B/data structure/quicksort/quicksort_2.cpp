#include <iostream>

using namespace std;

void quicksort(int *data, int start, int end){
    if (start >= end) {
        return;
    }

    int pivot = start, i = start + 1, j = end;
    while(i<j){
        while (i <= end && data[i] <= data[pivot]){
            i++;
        }
        while (j > start && data[j] >= data[pivot]){
            j--;
        }

        if (i > j){
            int temp = data[j];
            data[j] = data[pivot];
            data[pivot] = temp;
        } else {
            int temp = data[j];
            data[j] = data[i];
            data[i] = temp;
        }
    }

    quicksort(data, start, i-1);
    quicksort(data, j + 1, end);
}


int main(){
    int n = 10;
    int data[10] = {10,9,1,2,6,5,4,3,2,3};

    quicksort(data,0,9);

    for(int i=0;i<n;i++){
        cout << data[i] << " ";
    }
    cout << endl;

    return 0;
}
