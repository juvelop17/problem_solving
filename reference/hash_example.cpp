#include <cstdio>

using namespace std;

// Node, getKey, find, add, remove

#define HASH_SIZE (1<<18)
#define DIV (HASH_SIZE - 1)
#define MAX_N 100000


bool strCmp(const char a[], const char b[]) {
    int i;
    for (i = 0; a[i]; i++) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return a[i] == b[i];
}

void strCpy(char dst[], char src[]) {
    while (*src) {
        *dst++ = *src++;
    }
    *dst = 0;
}


struct Node {
    char key[11] = {};
    int data = -1;
    Node *next = nullptr;

    Node *alloc(char _key[], int _data, Node *_next) {
        strCpy(key, _key);
        data = _data;
        next = _next;
        return this;
    }

    Node *getPrevNode(char _key[]) {
        Node *prev = this;
        while (prev->next) {
            if (strCmp(prev->next->key, _key)) {
                break;
            }
            prev = prev->next;
        }
        return prev;
    }
};


Node nodePool[MAX_N];
int nodePoolCnt;

Node hashTable[HASH_SIZE];

void init() {
    nodePoolCnt = 0;
    for (int i = 0; i < HASH_SIZE; i++) {
        hashTable[i].next = nullptr;
    }}


long long getKey(const char key[]) {
    long long hash = 0;

    for (int i = 0; key[i]; ++i) {
        hash = ((hash << 5) + hash) + key[i] - 'a' + 1;
    }
    return hash & DIV;
}

int find(char key[]) {
    int target = getKey(key);
    Node *prevNode = hashTable[target].getPrevNode(key);

    return prevNode->next->data;
}

void add(char key[], int data) {
    int target = getKey(key);
    hashTable[target].next = nodePool[nodePoolCnt++].alloc(key, data, hashTable[target].next);
}

int remove(char key[]) {
    int target = getKey(key);
    Node *prevNode = hashTable[target].getPrevNode(key);
    Node *targetNode = prevNode->next;
    prevNode->next = prevNode->next->next;

    return targetNode->data;
}


int main() {
    add((char *) "a", 1);
    add((char *) "aa", 1);
    add((char *) "aaa", 1);
    add((char *) "aaaa", 1);
    add((char *) "aaaaa", 1);
    add((char *) "aaaaaa", 1);
    add((char *) "aaaaaaa", 1);
    add((char *) "aaaaaaaa", 1);
    add((char *) "aaaaaaaaa", 1);
    add((char *) "aaaaaaaaaa", 1);



    add((char *) "hello", 1);
    add((char *) "hello", 2);

    printf("%d \n", find((char *) "hello"));
    printf("%d \n", remove((char *) "hello"));
    printf("%d \n", remove((char *) "hello"));
    printf("%d \n", remove((char *) "hello"));

}







