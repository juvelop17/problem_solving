//
// Created by Junho Kim on 2021/09/09.
//

#include <iostream>




#include <string>
#include <vector>

using namespace std;

struct Trie;
Trie* alloc();

struct Trie {
    Trie *child[26];
    int cnt;

    void add(char *str) {
        if (*str == 0) {
            cnt++;
            return;
        }
        int idx = *str - 'a';
        if (idx >= 26 || idx < 0) {
            idx = 26;
        }
        if (child[idx] == nullptr) {
            child[idx] = alloc();
        }
        child[idx]->add(str + 1);
    }

    int count() {
        for (int i = 0; i < 26; ++i) {
            if (child[i]) {
                cnt += child[i]->count();;
            }
        }
        return cnt;
    }

    int find(char *str) {
        if (*str == '?') {
            return cnt;
        }
        int idx = *str - 'a';
        if (!child[idx]) {
            return 0;
        }
        return child[idx]->find(str + 1);
    }

    void clear() {
        for (int i = 0; i < 27; ++i) {
            child[i] = nullptr;
        }
    }
};

Trie *alloc() {
    Trie *trie = new Trie();
    trie->clear();
    trie->cnt = 0;
    return trie;
}

Trie *root[10001];
Trie *rroot[10001];

void reverse(char str[], string s) {
    for (int i = 0; i < s.size(); ++i) {
        str[i] = s[s.size() - 1 - i];
    }
    str[s.size()] = '\0';
}

vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> answer;
    for (int i = 0; i <= 10000; ++i) {
        root[i] = alloc();
        rroot[i] = alloc();
    }

    char rstr[10001];
    for (int i = 0; i < words.size(); ++i) {
        root[words[i].size()]->add((char*) (words[i].c_str()));
        reverse(rstr, words[i]);
        rroot[words[i].size()]->add(rstr);
    }

    for (int i = 0; i <= 10000; ++i) {
        root[i]->count();
        rroot[i]->count();
    }

    for (int i = 0; i < queries.size(); ++i) {
        int cnt = 0;
        if (queries[i][0] == '?') {
            reverse(rstr, queries[i]);
            cnt = rroot[queries[i].size()]->find(rstr);
        } else {
            cnt = root[queries[i].size()]->find((char*) queries[i].c_str());
        }
        answer.push_back(cnt);
    }

    return answer;
}




using namespace std;

int main() {
    vector<string> words = {"frodo", "front", "frost", "frozen", "frame", "kakao"};
    vector<string> queries = {"fro??", "????o", "fr???", "fro???", "pro?"};

    solution(words, queries);



    return 0;
}








