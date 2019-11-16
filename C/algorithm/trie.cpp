#include <iostream>
#include <cstring>

using namespace std;

struct Trie {
    bool finish;    //끝나는 지점을 표시해줌
    Trie* next[26];    //26가지 알파벳에 대한 트라이
    Trie() : finish(false) {
        memset(next, 0, sizeof(next));
    }
    ~Trie() {
        for (int i = 0; i < 26; i++)
            if (next[i])
                delete next[i];
    }
    void insert(const char* key) {
        if (*key == '\0')
            finish = true;    //문자열이 끝나는 지점일 경우 표시
        else {
            int curr = *key - 'A';
            if (next[curr] == NULL)
                next[curr] = new Trie();    //탐색이 처음되는 지점일 경우 동적할당
            next[curr]->insert(key + 1);    //다음 문자 삽입
        }
    }
    Trie* find(const char* key) {
        if (*key == '\0')return this;//문자열이 끝나는 위치를 반환
        int curr = *key - 'A';
        if (next[curr] == NULL)return NULL;//찾는 값이 존재하지 않음
        return next[curr]->find(key + 1); //다음 문자를 탐색
    }
};

struct Trie{
    Trie* next[10];
    bool term;
    Trie() : term(false){
        memset(next,0,sizeof(next));
    }
    ~Trie(){
        for(int i=0;i<10;i++){
            if(next[i])
                delete next[i];
        }
    }
    void insert(const char* key){
        if(*key=='\0')
            term=true;
        else{
            int curr = *key-'0';
            if(next[curr]==NULL)
                next[curr]=new Trie();
            next[curr]->insert(key+1);
        }
    }
    bool find(const char* key){
         if(*key=='\0')
            return 0;
        if(term)
            return 1;
        int curr = *key-'0';
        return next[curr]->find(key+1);
    }
};

int t,n,r;
char a[MAX_N][11];
int main(){
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        getchar();
        for(int i=0;i<n;i++)
            scanf("%s",&a[i]);
        Trie *root=new Trie;
        r=0;
        for(int i=0;i<n;i++)
            root->insert(a[i]);
        for(int i=0;i<n;i++){
            if(root->find(a[i])){
                r=1;
            }
        }
        printf("%s\n",r?"NO":"YES");
    }
    return 0;
}




