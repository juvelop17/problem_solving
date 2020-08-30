#include <iostream>
#include <vector>
#include <queue>
#include <time.h>

using namespace std;


int N, K, X, Y, W;
int delay[1001];
int in_degree[1001];
vector<int> graph[1001];
int vertex_delay[1001];

void array_print(int arr[]){
    for (int i=1;i<=N;i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}


int solution() {
    queue<int> que;

    for (int i=1;i<=N;i++){
        if (in_degree[i] == 0){
            que.push(i);
            vertex_delay[i] = delay[i];
        }
        
    }

    while (!que.empty()) {
        int cur = que.front();
        que.pop();
        for (int i=0;i<graph[cur].size();i++){
            int next = graph[cur][i];
            if (--in_degree[next] == 0) {
                que.push(next);
            }
            if (vertex_delay[next] < vertex_delay[cur] + delay[next]) {
                vertex_delay[next] = vertex_delay[cur] + delay[next];
            }
        }
    }

    // array_print(vertex_delay);

    return vertex_delay[W];
}

int main() {
    // freopen("input.txt","r",stdin);

    clock_t start, end;
    start = clock();

    int T;
    cin >> T;
    for (int i=0;i<T;i++){
        for(int j=1;j<1001;j++){
            graph[j].clear();
            in_degree[j] = 0;
            vertex_delay[j] = 0;
        }

        cin >> N >> K;
        for(int j=1;j<=N;j++){
            cin >> delay[j];
        }
        int num1, num2;
        for(int j=0;j<K;j++){
            cin >> num1 >> num2;
            graph[num1].push_back(num2);
            in_degree[num2]++;
        }
        cin >> W;
        cout << solution() << endl;
    }

    end = clock();
    // cout << end - start << endl;

    return 0;
}





