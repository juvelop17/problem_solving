#include <iostream>
#include <cstring>

using namespace std;


int t,n;
char pin[10][5];


struct Trie {
    bool finish;    
    int cnt;
    Trie* next[10];   
    Trie() : finish(false),cnt(0) {
        memset(next, 0, sizeof(next));
    }
    ~Trie() {
        for (int i = 0; i < 10; i++)
            if (next[i])
                delete next[i];
    }

    void insert(const char* key) {
        if (*key == '\0'){
            finish = true;
            cnt++;
        }
        else {
            int curr = *key - '0';
            if (next[curr] == NULL)
                next[curr] = new Trie();  
            next[curr]->insert(key + 1);   
        }
    }

    Trie* find(const char* key) {
        if (*key == '\0') return this;
        int curr = *key - '0';
        if (next[curr] == NULL) return this;
        return next[curr]->find(key + 1); 
    }
};


int solution(){
    Trie *root = new Trie;
    int cnt = 0;

    for (int i=0;i<n;i++){
        root->insert(pin[i]);
    }

    for (int i=0;i<n;i++){
        Trie *node = root->find(pin[i]);
        if (node->cnt > 1){
            cnt++;
            
            char num_tmp[5];
            strcpy(num_tmp,pin[i]);

            int pos = 3;
            num_tmp[pos]++;
            if (num_tmp[pos]-'0' == 10) {
                num_tmp[pos] = '0';
            }

            while(root->find(num_tmp)->cnt > 0) {
                num_tmp[pos]++;
                if (num_tmp[pos]-'0' == 10) {
                    num_tmp[pos] = '0';
                }
                if (num_tmp[pos] == pin[i][pos]){
                    pos--;
                    num_tmp[pos]++;
                    if (num_tmp[pos]-'0' == 10) {
                        num_tmp[pos] = '0';
                    }
                }
            }
            root->insert(num_tmp);
            strcpy(pin[i],num_tmp);
            node->cnt--;
        }
    }

    return cnt;
}

int main() {
    freopen("input.txt","r",stdin);

    cin >> t;
    for(int i=0;i<t;i++){
        cin >> n;
        for(int j=0;j<n;j++){
            cin >> pin[j];
        }
        cout << solution() << endl;
        for(int j=0;j<n;j++){
            cout << pin[j] << endl;
        }
    }
}
