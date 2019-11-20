#include <iostream>

using namespace std;

#define HEAP_SIZE 100

struct Heap {
    int heap[HEAP_SIZE];
    int heap_count = 0;

    void swap(int *a, int *b){
        int tmp = *a; *a = *b; *b = tmp;
    }

    void push(int data) {
        heap[++heap_count] = data;

        int child = heap_count;
        int parent = child / 2;
        while (child > 1 && heap[child] > heap[parent]){
            swap(&heap[parent],&heap[child]);
            child = parent;
            parent = child / 2;
        }
    }

    int pop() {
        int res = heap[1];
        swap(&heap[1],&heap[heap_count]);
        heap_count--;

        int parent = 1;
        int child = parent * 2;
        if (child + 1 <= heap_count) {
            child = heap[child] > heap[child + 1] ? child : child + 1;
        }
        while (child <= heap_count && heap[parent] < heap[child]) {
            swap(&heap[parent],&heap[child]);
            parent = child;
            child = parent * 2;
            if (child + 1 <= heap_count){
                child = heap[child] > heap[child + 1] ? child : child + 1;
            }
        }

        return res;
    }
};

int main() {
    int arr[10] = {1,2,3,5,10,6,1,30,2,1};

    Heap h;
    for(int i=0;i<10;i++){
        h.push(arr[i]);
    }

    for(int i=0;i<10;i++){
        cout << h.pop() << " ";
    }

    cout << endl;
    cout << sizeof(h);

    return 0;
}

