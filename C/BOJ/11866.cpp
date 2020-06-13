#include <iostream>
#include <vector>

using namespace std;

int N, K;

struct Llist {
    int num;
    Llist *next;
};

Llist *head;

int solution() {
    vector<int> vec;
    Llist *curr_node, *prev_node;

    prev_node = head;
    for(int i=0;i<N;i++){
        curr_node = prev_node->next;
        for(int j=0;j<K%N-1;j++){
            prev_node = curr_node;
            curr_node = curr_node->next;
        }
        vec.push_back(curr_node->num);
        prev_node->next = curr_node->next;
        delete curr_node;
    }

    cout << "<";
    for(int i=0;i<N-1;i++){
        cout << vec[i] << ", ";
    }
    cout << vec[N-1] << ">";

    return 0;
}

int main() {
    freopen("input.txt","r",stdin);

    cin >> N >> K;

    Llist dummy;
    dummy.num = 0;
    head = &dummy;
    Llist *prev_node = &dummy;
    
    for(int i=1;i<=N;i++){
        Llist *node = new Llist;
        node->num = i;
        node->next = NULL;
        prev_node->next = node;
        prev_node = node;
    }
    prev_node->next = head->next;

    solution();

    return 0;
}





