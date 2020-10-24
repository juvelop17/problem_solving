#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;


int N, mat[100 + 1][100 + 1];
int new_mat[100 + 1][100 + 1];
vector<vector<int>> vec;
vector<bool> visited;

void print_matrix(int mat[][101]) {
	int i, j;

	for (i = 1; i <= N; i++) {
		for (j = 1; j <= N; j++) {
			printf("%d ", mat[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

void dfs(int num) {
	int i, j;

	//cout << "------------------------" << endl;
	//cout << "num : " << num << endl;
	//print_matrix(mat);
	//print_matrix(new_mat);
	//cout << "------------------------" << endl;

	for (int next : vec[num]) {
		if (!visited[next]) {
			visited[next] = true;
			dfs(next);
		}
	}
}

int main() {
	int i, j;
	scanf("%d", &N);

	vec.resize(N+1);
	for (i = 1; i <= N; i++) for (j = 1; j <= N; j++) scanf("%d", &mat[i][j]);
	for (i = 1; i <= N; i++) for (j = 1; j <= N; j++) new_mat[i][j] = 0;
	for (i = 1; i <= N; i++)
		for (j = 1; j <= N; j++)
			if (mat[i][j] == 1) {
				vec[i].push_back(j);
			}
	for (i = 1; i <= N; i++) {
		visited.clear();
		visited.resize(N+1, false);
		dfs(i);

		for (j = 1; j <= N; j++) {
			if (visited[j]) {
				new_mat[i][j] = 1;
			}
		}
	}

	print_matrix(new_mat);
}
