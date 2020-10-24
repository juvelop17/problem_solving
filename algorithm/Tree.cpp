#include <iostream>

using namespace std;

typedef struct Node {
    int num;
    int delay;
    bool visited = false;
    Node *brother = NULL;
    Node *child = NULL;

    Node() {}
    Node(int num, int delay):num(num),delay(delay) {}

    void insertNode(int num, int delay){
        Node *new_node = new Node(num, delay);
        Node *cur = child;
        if (cur == NULL) {
            child = new_node;
            return;
        }
        while (cur != NULL) {
            if (cur->brother == NULL) {
                cur->brother = new_node;
            }
            cur = cur->brother;
        }
    }
} Node;

typedef struct Tree {
    Node *root;
} Tree;