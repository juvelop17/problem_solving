#include <iostream>

using namespace std;


#define MAX_KEY 64
#define MAX_DATA 128
#define MAX_TABLE 4096

#define DELETE_COUNT 6
#define FIND_COUNT 8


struct Node {
    char key[MAX_KEY + 1];
    int value;
    Node *next;
};
Node *tb[MAX_TABLE];

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

void my_strcpy(char *dest, const char *src){
    while(*src != '\0') {
        *dest = *src;
        dest++; src++;
    }
    *dest = '\0';
}

int my_strcmp(const char *str1, const char *str2){
    while (*str1 != '\0' && (*str1 == *str2)) {
        str1++;
        str2++;
    }
    return *str1 - *str2;
}


int getHash(const char *str) {
    int hash = 5381;
    int c = *str;

    while (*str != '\0') {
        hash = (((hash << 5) + hash) + c) % MAX_TABLE;
        str++;
    }

    return hash % MAX_TABLE;
}


bool find(const char *key, int *val){
    int h = getHash(key);
    Node *cur = tb[h];
    while (cur != NULL) {
        if (my_strcmp(cur->key,key) == 0){
            *val = cur->value;
            return true;
        }
        cur = cur->next;
    }

    return false;
}


void add(const char *key, int value){
    Node *new_node = new Node;
    my_strcpy(new_node->key,key);
    new_node->value = value;
    new_node->next = NULL;

    int h = getHash(key);

    if(tb[h] == NULL){
        tb[h] = new_node;
    } else {
        Node *cur = tb[h];
        while (cur != NULL) {
            if(my_strcmp(cur->key,key) == 0) {
                cur->value = value;
                return;
            }
            cur = cur->next;
        }
        new_node->next = tb[h];
        tb[h] = new_node;
    }
}


bool destroy(const char *key){
    int h = getHash(key);

    if(tb[h] == NULL) {
        return false;
    }

    if (my_strcmp(tb[h]->key,key) == 0){
        Node *first = tb[h];
        tb[h] = tb[h]->next;
        free(first);
        return true;
    } else {
        Node *cur = tb[h]->next;
        Node *prev = tb[h];

        while (cur != NULL && my_strcmp(cur->key,key) != 0){
            prev = cur;
            cur = cur -> next;
        }

        if (cur == NULL) return false;

        prev->next = cur->next;
        free(cur);
        return true;
    }
}

void print_hash() {
	for (int i = 0; i < MAX_TABLE; ++i) {
		if (tb[i] != NULL) {
			printf("index : %d\n", i);
			Node * cur = tb[i];
			while (cur != NULL) {
				printf("{ %s, %d }, ", cur->key, cur->value);
				cur = cur->next;
			}
			printf("\n");
		}
	}
}


int main(int argc, char* argv[])
{
    int T, N, Q;
    freopen("input.txt","r",stdin);

    cin >> T;
 
    for (int test_case = 1; test_case <= T; test_case++)
    {
        memset(tb, 0, sizeof(tb));
        cin >> N;
        char k[MAX_KEY + 1];
        // char d[MAX_DATA + 1];
        int val;

        cout << "#" << test_case << endl;
 
        for (int i = 0; i < N; i++)
        {
            cin >> k >> val;
            cout << k << "\t" << val << endl;
            add(k, val);
        }

        cout << endl;
        print_hash();
        cout << endl;
 
        cin >> Q;
        for (int i = 0; i < Q; i++)
        {
            char k[MAX_KEY + 1];
            // char d[MAX_DATA + 1];
            int val;
 
            cin >> k;
            if (find(k, &val))
            {
                cout << val << endl;;
            }
            else
            {
                cout << "not find\n";
            }
        }
        cout << endl;
    }
    return 0;
}




