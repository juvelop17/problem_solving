#include <iostream>

using namespace std;

void swap(int *a, int *b){
    int temp = *a; *a = *b; *b = temp;
}


void quicksort(int data[][2], int start, int end){
    if (start >= end){
        return;
    }

    int pivot = start, i = start + 1, j = end;

    while (i < j){
        while (i <= end && data[i][0] <= data[pivot][0]){
            i++;
        }
        while (j > start && data[j][0] >= data[pivot][0]) {
            j--;
        }

        if (i > j){
            swap(data[j][0],data[pivot][0]);
            swap(data[j][1],data[pivot][1]);
        } else {
            swap(data[j][0],data[i][0]);
            swap(data[j][1],data[i][1]);
        }
    }

    quicksort(data, start, j-1);
    quicksort(data, j+1, end);
}


int main() {
    int d[10][2] = {{1,1},
                {2,1},
                {10,1},
                {1,2},
                {3,1},
                {1,3},
                {2,2},
                {3,2},
                {8,1},
                {1,4}};




    for (int i=0;i<9;i++){
        cout << d[i][0] << " " << d[i][1] << endl;
    }
    cout << endl;

    quicksort(d,0,9);

    for (int i=0;i<10;i++){
        cout << d[i][0] << " " << d[i][1] << endl;
    }

    cout << endl;
    cout << "d : " << d << endl;
    cout << "d[1] : " << d[1] << endl;
    cout << "&d[1] : " << &d[1] << endl;
    cout << "*d[1] : " << *d[1] << endl;
    cout << "&d[1][0] : " << &d[1][0] << endl;
    cout << "&d[1][1] : " << &d[1][1] << endl;
    cout << "d[1][0] : " << d[1][0] << endl;
    cout << "d[1][1] : " << d[1][1] << endl;
    // cout << "*d[1] : " << *d[1][0] << endl;
    // cout << "*d[1] : " << *d[1][1] << endl;


    int *temp = d[1];
    cout << "temp : " << temp << endl;
    cout << "*temp : " << *temp << endl;
}



