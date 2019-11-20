#include <iostream>

using namespace std;

#define HEAP_SIZE 256
#define ARRAY_SIZE 10

int heap[HEAP_SIZE];
int heap_count = 0;

void swap(int *a, int *b){
    int tmp = *a; *a = *b; *b = tmp;
}

void init(){
    heap_count = 0;
}

int size(){
    return heap_count;
}

void push(int data){
    heap[++heap_count] = data;

    int child = heap_count;
    int parent = child / 2;
    while (child > 1 && heap[parent] < heap[child]){
        swap(&heap[parent], &heap[child]);
        child = parent;
        parent = child / 2;
    }
}

int pop(){
    int result = heap[1];
    swap(&heap[1],&heap[heap_count]);
    heap_count--;

    int parent = 1;
    int child = parent * 2;
    if (child + 1 <= heap_count) {
        child = (heap[child] > heap[child + 1]) ? child : child + 1;
    }

    while (child <= heap_count && heap[parent] < heap[child]) {
        swap(&heap[parent],&heap[child]);
        parent = child;
        child = child * 2;
        if(child + 1 <= heap_count){
            child = (heap[child] > heap[child+1]) ? child : child + 1;
        }
    }

    return result;
}

#include <time.h>

int main(){
    int arr[ARRAY_SIZE];

    srand(time(NULL));
    // 배열 초기화
	for (int i = 0; i < ARRAY_SIZE; i++) {
		// 1 ~ 50까지의 난수 생성
		arr[i] = rand() % 50 + 1;
	}

	// 삽입
	for (int i = 0; i < ARRAY_SIZE; i++) {
		push(arr[i]);
	}

	// pop 하면서 값들 하나씩 확인
	// Max Heap이기 때문에 값들이 내림차순으로 정렬됨 -> Heap Sort
	for (int i = 0; i < ARRAY_SIZE; i++) {
		printf("%d ", pop());
	}
	printf("\n");

	return 0;
}

