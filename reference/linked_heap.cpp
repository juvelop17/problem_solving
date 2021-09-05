//
// Created by Junho Kim on 2021/08/24.
//


#include <iostream>

using namespace std;


#define HEAP_POOL_SIZE 1000




struct HeapNode {
    int value;
    HeapNode *parent;
    HeapNode *child[2];

    HeapNode *alloc(int _value, HeapNode *_parent, HeapNode *_child[]) {
        value = _value;
        parent = _parent;
        for (int i = 0; i < 2; i++) {
            child[i] = _child[i];
        }
        return this;
    }
};

HeapNode heapPool[HEAP_POOL_SIZE];
int heapPoolCnt;


struct Heap {
    HeapNode *root;
    int size;

    void init() {
        size = 0;
    }

    HeapNode *create(int value) {
        HeapNode *child[2] = {nullptr,};
        HeapNode *cur = heapPool[heapPoolCnt++].alloc(value, nullptr, child);
        return cur;
    }

    HeapNode *findNode(int idx) {
        if (idx == 1) return root;
        return findNode(idx >> 1)->child[idx & 1];
    }

    bool compare (HeapNode *node1, HeapNode *node2) {
        return node1->value < node2->value;
    }

    void push(int value) {
        if (size + 1 >= HEAP_POOL_SIZE) {
            printf("heap is full\n");
            return;
        }
        size++;
        HeapNode *cur = create(value);
        if (size == 1) {
            root = cur;
            return;
        }

        HeapNode *parent = findNode(size >> 1);
        parent->child[size & 1] = cur;
        cur->parent = parent;
        while (cur->parent && compare(cur, cur->parent)) {
            int tmp = cur->value;
            cur->value = cur->parent->value;
            cur->parent->value = tmp;

            cur = cur->parent;
        }
    }

    int pop() {
        if (size <= 0) {
            printf("heap is empty\n");
            return -1;
        }

        int value = root->value;
        if (size == 1) {
            return value;
        }

        HeapNode *cur = findNode(size);
        root->value = cur->value;
        cur->parent->child[size & 1] = nullptr;
        size--;

        cur = root;
        while (cur->child[0] != nullptr) {
            HeapNode *child;
            if (cur->child[1] == nullptr) {
                child = cur->child[0];
            }
            else {
                child = compare(cur->child[0], cur->child[1]) ? cur->child[0] : cur->child[1];
            }

            if (cur->value <= child->value) {
                break;
            }

            int tmp = cur->value;
            cur->value = child->value;
            child->value = tmp;

            cur = child;
        }
        return value;
    }

    int top() {
        return root->value;
    }

};

Heap heap;

void heapInit() {
    heapPoolCnt = 0;
    heap.init();
}


int main() {
    heapInit();

    heap.push(1);
    heap.push(2);
    heap.push(3);
    heap.push(4);
    heap.push(5);

    printf("%d\n", heap.pop());
    printf("%d\n", heap.pop());
    printf("%d\n", heap.pop());
    printf("%d\n", heap.pop());
    printf("%d\n", heap.pop());
}










