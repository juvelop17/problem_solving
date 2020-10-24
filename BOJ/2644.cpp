#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

int n, x, y, m;
vector<vector<int>> vec;
vector<bool> visited;
vector<int> level_vec;

int bfs(int x, int y) {
	int i, j, node, que_size, level;
	queue<int> que;

	que.push(x);
	visited[x] = true;
	level_vec[x] = 0;

	level = 0;
	while (!que.empty()) {
		que_size = que.size();

		//cout << "level " << level << endl;
		for (i = 0; i < que_size; i++) {
			node = que.front();
			que.pop();
			//cout << "node " << node << endl;
			if (node == y) {
				return level;
			}
			for (int next : vec[node]) {
				if (!visited[next]) {
					visited[next] = true;
					level_vec[next] = level;
					que.push(next);
				}
			}
		}
		level++;
	}

	return -1;
}

int main() {
	int i, j, a, b;
	scanf("%d", &n);
	scanf("%d", &x);
	scanf("%d", &y);
	scanf("%d", &m);

	vec.resize(n+1);
	visited.resize(n + 1, false);
	level_vec.resize(n + 1, 0);

	for (i = 0; i < m; i++) {
		scanf("%d", &a);
		scanf("%d", &b);

		vec[a].push_back(b);
		vec[b].push_back(a);
	}

	printf("%d",bfs(x, y));
}
