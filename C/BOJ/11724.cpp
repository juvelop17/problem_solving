#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;

int N, M, a,b;
vector<vector<int>> vec;	// 간선 연결
vector<bool> visited;


int dfs(int n) {
	int i, cnt = 0;
	//cout << "node " << n << "visited." << endl;

	for (int next : vec[n]) {
		if (!visited[next]) {
			visited[next] = true;
			cnt += dfs(next);
			cnt++;
		}
	}

	return cnt;
}


int main() {
	int i, connected_cnt = 0;

	scanf("%d", &N);
	scanf("%d", &M);

	vec.resize(N+1);
	visited.resize(N+1, false);

	for (i = 1; i <= M; i++) {
		scanf("%d", &a);
		scanf("%d", &b);

		// 간선 연결
		vec[a].push_back(b);
		vec[b].push_back(a);
	}

	for (i = 1; i <= N; i++) {
		if (!visited[i]) {
			//cout << "-----------------------------" << endl;
			visited[i] = true;
			dfs(i);
			connected_cnt++;
		}
	}

	printf("%d", connected_cnt);
}
