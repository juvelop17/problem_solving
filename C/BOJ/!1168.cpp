#include <iostream>
#include <vector>

using namespace std;

int N, K;
int num_list[1000001];

int solution() {
    vector<int> vec;

    int curr;
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

    
    for(int i=1;i<=N;i++){
        num_list[i] = i
    }

    solution();

    return 0;
}





