#include <iostream>

using namespace std;



template <class K, class V>
class map{
public:
    struct Node{
        Node *l, *r, *p;
        K key;
        T val;
    }
    
    Node *root;
    map():root(0){}
    ~map(){
        while (root) erase(root->key);
    }
    void rotate(Node *x){
        
    }
    

}













#define MAX_TABLE 5
#define MAX_KEY 8
#define MAX_DATA 12

#define DELETE_COUNT 6
#define FIND_COUNT 8


struct Node {
    char key[MAX_KEY];
    int value;
    Node *next;
};

Node *tb[MAX_TABLE];
char keys[MAX_DATA][MAX_KEY];
int values[MAX_DATA];


void init(){
    for(int i=0;i<MAX_TABLE;++i){
        Node *cur = tb[i];
        Node *tmp;
        while(cur != NULL) {
            tmp = cur;
            cur = cur -> next;
            free(tmp);
        }
        tb[i] = NULL;
    }

    // 미완성
}

void my_str_cpy(char *dest, const char *src){
    while(*src != '\0') {
        *dest = *src;
        dest++; src++;
    }
    *dest = '\0';
}

int my_str_cmp(const char *str1, const char *str2){
    while (*str1 != '\0' && (*str1 == *str2)) {
        str1++;
        str2++;
    }
    return *str1 - *str2;
}

int hash(const char *str) {
    int hash = 401;
    int c;

    while (*str != '\0') {
        hash = ((hash << 4) + (int)(*str)) % MAX_TABLE;
        str++;
    }

    return hash % MAX_TABLE;
}

void add(const char *key, int value){
    Node *new_node = new Node;
    my_str_cpy(new_node->key,key);
    new_node->value = value;
    new_node->next = NULL;

    int index = hash(key);

    if(tb[index] == NULL){
        tb[index] = new_node;
    } else {
        Node *cur = tb[index];
        while (cur != NULL) {
            if(my_str_cmp(cur->key,key) == 0) {
                cur->value = value;
                return;
            }
            cur = cur->next;
        }
        new_node->next = tb[index];
        tb[index] = new_node;
    }
}

bool find(const char *key, int *val){
    int index = hash(key);
    Node *cur = tb[index];
    while (cur != NULL) {
        if (my_str_cmp(cur->key,key) == 0){
            *val = cur->value;
            return true;
        }
        cur = cur->next;
    }

    return false;
}

bool destory(const char *key) {
    int index = hash(key);

    if (tb[index] == )
}




