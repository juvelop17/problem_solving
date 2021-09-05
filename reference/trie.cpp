//
// Created by Junho Kim on 2021/08/19.
//

#include <iostream>

#define ALPHA_CNT 26
#define MAX_N 100






struct Trie;
Trie* alloc();

struct Trie {
    Trie *child[ALPHA_CNT];

    void add(char *str) {
        if (*str == 0) return;
        if (child[*str-'a'] == nullptr) child[*str-'a'] = alloc();
        child[*str-'a']->add(str+1);
    }

    Trie *get(char *str) {
        if (*str == 0) return this;
        if (child[*str - 'a'] == nullptr) return nullptr;
        return child[*str - 'a']->get(str + 1);
    }

    void clear() {
        for (int i = 0; i < ALPHA_CNT; i++) {
            child[i] == nullptr;
        }
    }
};

Trie node[MAX_N];
int nodeCnt;
Trie *root;

Trie* alloc() {
    Trie *cur = &node[nodeCnt++];
    cur->isTerminal = false;
    cur->clear();
    return cur;
}

void trieInit() {
    nodeCnt = 0;
    root = alloc();
}




int main() {
    trieInit();

    root->add("hello");
    root->add("hi");
    printf("hello %d\n", root->get("hello") != nullptr ? root->get("hello")->isTerminal : -1);
    printf("hi %d\n", root->get("hi") != nullptr ? root->get("hi")->isTerminal : -1);
    printf("he %d\n", root->get("he") != nullptr ? root->get("he")->isTerminal : -1);

    root->add("he");
    printf("he %d\n", root->get("he") != nullptr ? root->get("he")->isTerminal : -1);
}

