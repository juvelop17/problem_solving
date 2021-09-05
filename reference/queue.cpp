//
// Created by Junho Kim on 2021/08/20.
//

#define QUE_SIZE 100;

struct Queue {
    int arr[QUE_SIZE];
    int head = 0;
    int tail = 0;

    bool isEmpty() {
        return head == tail;
    }

    bool isFull() {
        return (tail + 1) % QUE_SIZE == head
    }

    void enqueue(int data) {
        if(isFull()) {
            return;
        }
        arr[tail++] = data;
        tail %= QUE_SIZE;
    }

    int dequeue() {
        if (isEmpty()) {
            return;
        }
        int data = arr[head++];
        head %= QUE_SIZE;
        return data;
    }
};


