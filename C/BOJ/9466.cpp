#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;

// tc_num : 테스트 케이스 개수
// n : 학생 수
// m : 학생 번호

int n, m[100001], tc_num;
vector<bool> visited;
vector<bool> finished;
int cnt;
int cnt_array[100];

void dfs(int node) {
	int next = m[node];
	if (!visited[next]) {
		visited[next] = true;
		dfs(next);
	}
	else if (visited[next] && !finished[next]) {
		for (int i = next; i != node; i = m[i])
			cnt++;
		cnt++;
	}
	finished[node] = true;
}

int main() {
	int i, j;

	scanf("%d", &tc_num);

	for (i = 0; i < tc_num; i++) {
		scanf("%d", &n);
		for (j = 1; j <= n; j++) {
			scanf("%d", &m[j]);
		}

		cnt = 0;
		visited.clear();
		finished.clear();
		visited.resize(n + 1, false);
		finished.resize(n + 1, false);

		for (j = 1; j <= n; j++) {
			if (!visited[j]) {
				visited[j] = true;
				dfs(j);
			}
		}
		cout << n - cnt << endl;
	}
}
