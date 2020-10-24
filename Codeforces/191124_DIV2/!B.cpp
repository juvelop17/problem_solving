#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int t, n;
vector<int> vec;


struct Node {
    bool visited;
    int val;
    Node *prev;
    Node *next;

    Node () : visited(false), val(-1), prev(NULL), next(NULL) {}
    Node (int v, Node *p, Node *n) : visited(false), val(v), prev(p), next(n) {}
};

int solution() {
    vector<Node*> node_list(n);
    vector<int> res;

    int mx = 0;
    int mn = 0;
    int num, cur;

    node_list[1]->next = node_list[2];
    node_list[1]->prev = NULL;
    node_list[1]->val = 1;
    node_list[n]->next = NULL;
    node_list[n]->prev = node_list[n-1];
    node_list[n]->val = n;
    for (int i=2;i<n;i++){
        Node *new_node = new Node(i,node_list[i-1],node_list[i+1]);
        node_list[i] = new_node;
    }

    for(int i=0;i<n;i++){
        cur = vec[i];
        if (mx < cur) {
            mx = cur;
            num = cur;
        } else {
            num = mn;
            mn = node_list[mn]->next->val;
        }
        
        if (node_list[num]->visited) {
            cout << -1 << endl;
            return -1;
        }
        node_list[num]->visited = true;

        if (node_list[num]->next != NULL && node_list[num]->prev != NULL){
            node_list[num]->prev->next = node_list[num]->next;
            node_list[num]->next->prev = node_list[num]->prev;
        } else if (num == 1){
            node_list[num]->next->prev = node_list[num]->prev;
        } else if (num == n){
            node_list[num]->prev->next = node_list[num]->next;
        }
        
        res.push_back(num);
    }

    for (int i=0;i<n;i++){
        cout << res[i] << " ";
    }
    cout << endl;

    return 0;
}

int main() {
    // freopen("input.txt","r",stdin);

    cin >> t;
    for(int test_case=0;test_case<t;test_case++){
        cin >> n;
        int num;
        for(int i=0;i<n;i++){
            cin >> num;
            vec.push_back(num);
        }
        solution();
    }
}




