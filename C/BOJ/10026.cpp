#include <iostream>
using namespace std;

char mat[100][100];
bool visited[100][100];
int N;

void print_matrix() {
	int i, j;

	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			printf("%c ", visited[i][j]);
		}
		cout << endl;
	}
}


void dfs(int x, int y, char color) {
	visited[x][y] = true;
	//cout << "----------------------" << endl;
	//cout << "color : " << color << endl;
	//print_matrix();
	//cout << "----------------------" << endl;

	if (x - 1 >= 0 && !visited[x - 1][y] && color == mat[x-1][y]) dfs(x - 1, y, color);
	if (x + 1 < N && !visited[x + 1][y] && color == mat[x + 1][y]) dfs(x + 1, y, color);
	if (y - 1 >= 0 && !visited[x][y - 1] && color == mat[x][y-1]) dfs(x, y - 1, color);
	if (y + 1 < N && !visited[x][y + 1] && color == mat[x][y+1]) dfs(x, y + 1, color);
}

void redgreen_dfs(int x, int y, char color) {
	visited[x][y] = true;
	//cout << "----------------------" << endl;
	//cout << "color : " << color << endl;
	//print_matrix();
	//cout << "----------------------" << endl;

	if (color == 'R' || color == 'G') {
		if (x - 1 >= 0 && !visited[x - 1][y] && 'B' != mat[x - 1][y]) redgreen_dfs(x - 1, y, color);
		if (x + 1 < N && !visited[x + 1][y] && 'B' != mat[x + 1][y]) redgreen_dfs(x + 1, y, color);
		if (y - 1 >= 0 && !visited[x][y - 1] && 'B' != mat[x][y - 1]) redgreen_dfs(x, y - 1, color);
		if (y + 1 < N && !visited[x][y + 1] && 'B' != mat[x][y + 1]) redgreen_dfs(x, y + 1, color);
	}
	else {
		if (x - 1 >= 0 && !visited[x - 1][y] && 'B' == mat[x - 1][y]) redgreen_dfs(x - 1, y, color);
		if (x + 1 < N && !visited[x + 1][y] && 'B' == mat[x + 1][y]) redgreen_dfs(x + 1, y, color);
		if (y - 1 >= 0 && !visited[x][y - 1] && 'B' == mat[x][y - 1]) redgreen_dfs(x, y - 1, color);
		if (y + 1 < N && !visited[x][y + 1] && 'B' == mat[x][y + 1]) redgreen_dfs(x, y + 1, color);
	}
}



int main() {
	int i, j, k, cnt[2];

	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		scanf("%s", mat[i]);
	}

	// 정상
	cnt[0] = 0;
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			visited[i][j] = false;
		}
	}

	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			if (!visited[i][j]) {
				dfs(i, j, mat[i][j]);
				cnt[0]++;
			}
		}
	}

	// 색약
	cnt[1] = 0;
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			visited[i][j] = false;
		}
	}

	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			if (!visited[i][j]) {
				redgreen_dfs(i, j, mat[i][j]);
				cnt[1]++;
			}
		}
	}

	printf("%d %d", cnt[0], cnt[1]);
}

