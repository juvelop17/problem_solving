#include <cstdio>
#include <iostream>
using namespace std;

char mat[100][100], visited[100][100];
int N, height, height_cnt[101];
int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,-1,1 };

void matrix_init(char m[][100], int val) {
	int i, j;
	
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			m[i][j] = val;
		}
	}
}

void dfs(int x, int y, int height) {
	int i, j;
	int cx, cy;

	visited[x][y] = true;
	//cout << x << " " << y << endl;

	for (i = 0; i < 4; i++) {
		cx = x + dx[i];
		cy = y + dy[i];
		if (cx >= 0 && cx < N && cy >= 0 && cy < N &&
			mat[cx][cy] > height && !visited[cx][cy]) {
			dfs(cx, cy, height);
		}
	}
}

int main() {
	int i, j, height, max;

	scanf("%d", &N);
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			scanf("%d", &mat[i][j]);
		}
	}

	for (j = 1; j <= 100; j++) {
		height_cnt[j] = 0;
	}

	for (height = 1; height <= 100; height++) {
		//cout << "----------------------------------------" << endl;
		matrix_init(visited, false);

		for (i = 0; i < N; i++) {
			for (j = 0; j < N; j++) {
				if (!visited[i][j] && mat[i][j] > height) {
					dfs(i, j, height);
					height_cnt[height]++;
				}
			}
		}
	}

	max = 1;
	for (j = 1; j <= 100; j++) {
		if (height_cnt[j] > max)
			max = height_cnt[j];
	}
	printf("%d", max);

	return 0;
}