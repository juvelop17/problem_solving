#include <iostream>

using namespace std;
 
#define MAX_KEY 64
#define MAX_DATA 128
#define MAX_TABLE 4096
 
struct Data {
    int a;
    int b;
    int c;

    Data () : a(0), b(0), c(0) {}
};

struct Hash{
    char key[MAX_KEY + 1];
    Data *data;
    Hash *next;
};
Hash *tb[MAX_TABLE];

unsigned long getHash(const char *str)
{
    unsigned long hash = 5381;
    int c = *str++;
 
    while (c)
    {
        hash = (((hash << 5) + hash) + c) % MAX_TABLE;
        c = *str++;
    }
 
    return hash % MAX_TABLE;
}
 
bool find(const char *key, Data *data)
{
    unsigned long h = getHash(key);
    Hash *cur = tb[h];
 
    while (cur != NULL) 
    {
        if (strcmp(cur->key, key) == 0)
        {   
            data->a = cur->data->a;
            data->b = cur->data->b;
            data->c = cur->data->c;
            return true;
        }
        cur = cur->next;
    }
    return false;
}
 
int add(char *key, Data *data)
{
    unsigned long h = getHash(key);
    Hash *cur = tb[h];
 
    while (cur != NULL)
    {
        if (strcmp(cur->key, key) == 0)
        {   
            cur->data->a = data->a;
            cur->data->b = data->b;
            cur->data->c = data->c;
            return 0;
        }
 
        cur = cur->next;
    }
    Hash *new_hash = new Hash;
    strcpy(new_hash->key, key);
    new_hash->data->a = data->a;
    new_hash->data->b = data->b;
    new_hash->data->c = data->c;
    new_hash->next = NULL;
    tb[h] = new_hash;

    return 1;
}

void destroy(const char *key) {
    unsigned long h = getHash(key);
    Hash *cur = tb[h];

    if (cur == NULL) {
        return;
    }

    if (strcmp(cur->key,key) == 0) {
        tb[h] = cur->next;
        free(cur);
        return;
    } else {
        Hash *prev = cur;
        cur = cur->next;
        while (cur != NULL) {
            if (strcmp(cur->key,key) == 0) {
                prev->next = cur->next;
                free(cur);
                return;
            }
            cur = cur->next;
        }
    }

    return;
}


void print_hash() {
    for(int i=0;i<MAX_TABLE;i++){
        cout << i << " : ";
        Hash *cur = tb[i];
        while(cur != NULL){
            cout << "(" << cur->key << "," << cur->data->a << ") ";
            cur = cur->next;
        }
        cout << endl;
    }
}


int main(int argc, char* argv[])
{
    int T, N, Q;
    freopen("input.txt","r",stdin);

    cin >> T;
 
    for (int test_case = 1; test_case <= T; test_case++) {
        memset(tb, 0, sizeof(tb));
        cin >> N;
        char k[MAX_KEY + 1];
        // char d[MAX_DATA + 1];
        Data *val = new Data;

        cout << "#" << test_case << endl;
 
        for (int i = 0; i < N; i++)
        {
            cin >> k >> val->a;
            cout << k << "\t" << val->a << endl;
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
            Data *val;
 
            cin >> k;
            if (find(k, val))
            {
                cout << val->a << endl;;
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
