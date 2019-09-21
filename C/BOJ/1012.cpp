#include <cstdio>
#include <vector>
using namespace std;

// M : 가로
// N : 세로
// K : 배추 위치 개수

int N, M, K, tc_num;
int matrix[50][50];
bool visited[50][50];
int worm_cnt[50];


int dfs(int x, int y) {
	if (x - 1 >= 0) {
		if (!visited[x - 1][y] && matrix[x - 1][y] == 1) {
			visited[x - 1][y] = true;
			dfs(x - 1, y);
		}
	}
	if (x + 1 < M) {
		if (!visited[x + 1][y] && matrix[x + 1][y] == 1) {
			visited[x + 1][y] = true;
			dfs(x + 1, y);
		}
	}
	if (y - 1 >= 0) {
		if (!visited[x][y - 1] && matrix[x][y - 1] == 1) {
			visited[x][y - 1] = true;
			dfs(x, y - 1);
		}
	}
	if (y + 1 < N) {
		if (!visited[x][y + 1] && matrix[x][y + 1] == 1) {
			visited[x][y + 1] = true;
			dfs(x, y + 1);
		}
	}

	return 0;
}


int main() {
	int i, j;
	int a, b;
	int x, y;

	for (i = 0; i < 50; i++) {
		worm_cnt[i] = 0;
	}
	scanf("%d", &tc_num);
	
	for (i = 0; i < tc_num; i++) {
		for (int s = 0; s < 50; s++) {
			for (int t = 0; t < 50; t++) {
				matrix[s][t] = 0;
				visited[s][t] = false;
			}
		}

		scanf("%d", &M);
		scanf("%d", &N);
		scanf("%d", &K);

		for (j = 0; j < K; j++) {
			scanf("%d", &a);
			scanf("%d", &b);

			matrix[a][b] = 1;
		}

		for (x = 0; x < M; x++) {
			for (y = 0; y < N; y++) {
				if (!visited[x][y] && matrix[x][y] == 1) {
					visited[x][y] = true;
					dfs(x, y);
					worm_cnt[i]++;
				}
			}
		}
	}

	for(i=0;i<tc_num;i++)
		printf("%d\n", worm_cnt[i]);

}