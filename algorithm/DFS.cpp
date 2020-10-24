#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Graph {
public:
	int N;	// 정점 개수
	vector<vector<int>> vec;	// 인접 리스트
	vector<bool> visited;
	
	Graph() { N = 0; }
	Graph(int n) { 
		N = n; 
		vec.resize(n);
		visited.resize(N, false);
	}

	void addEdge(int u, int v) {
		vec[u].push_back(v);
		vec[v].push_back(u);
	}

	void sortList() {
		for (int i = 0; i < N; i++) {
			sort(vec[i].begin(), vec[i].end());
		}
	}

	void dfs() {
		dfs(0);
	}

	void dfs(int current) {
		visited[current] = true;
		cout << "node " << current << " 방문" << endl;
		
		for (int next : vec[current]) {
			if (visited[next] != true) {
				dfs(next);
			}
		}
	}
};


int main() {
	Graph G(9);
	G.addEdge(0, 1);
	G.addEdge(0, 2);
	G.addEdge(1, 3);
	G.addEdge(1, 5);
	G.addEdge(3, 4);
	G.addEdge(4, 5);
	G.addEdge(2, 6);
	G.addEdge(2, 8);
	G.addEdge(6, 7);
	G.addEdge(6, 8);
	G.sortList();
	G.dfs();
}




