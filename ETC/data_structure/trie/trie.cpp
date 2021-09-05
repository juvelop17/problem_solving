#include <iostream>

using namespace std;

struct Trie {
    bool isFinish;
    Trie *next[26];

    Trie () : isFinish(false) {
        memset(next,NULL,sizeof(next));
    }

    void insert(const char *key){
        if (*key == '\0') {
            isFinish = true;
            return;
        }
        int cur = *key - 'A';
        if (next[cur] == NULL) {
            Trie *new_trie = new Trie;
            next[cur] = new_trie;
        }
        next[cur]->insert(key + 1);
    }

    Trie* find(const char* key) {
        if (*key == '\0') {
            return this;
        }
        int cur = *key - 'A';
        if (next[cur] == NULL) {
            return NULL;
        }
        return next[cur]->find(key + 1);
    }
}