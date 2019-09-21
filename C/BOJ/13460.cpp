#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;

// . :빈칸
// # : 벽
// o : 구멍
// R : 빨간구슬
// B : 파란구슬


int N, M;
char board[10][10];
int ans, ex, ey;

void dfs(int rx, int ry, int bx, int by, int dx, int dy, int cnt) {
	int move_red = 0, move_blue = 0;

	if (cnt > 10 || cnt > ans) {
		return;
	}

	//printf("%d,%d %d,%d   cnt %d\n", rx, ry, bx, by, cnt);

	if (dx != 0 || dy != 0) {
		// blue 이동
		while (board[bx + dx][by + dy] != '#') {
			bx += dx; by += dy; move_blue++;
			if (board[bx][by] == 'O') {
				return;
			}
		}

		// red 이동
		while (board[rx + dx][ry + dy] != '#') {
			rx += dx; ry += dy; move_red++;
			if (board[rx][ry] == 'O') {
				if (cnt < ans) ans = cnt;
				//printf("목표 도달 %d %d %d %d\n", dx, dy, ans, cnt);
				return;
			}
		}
	}

	// 겹치는 경우
	if (rx == bx && ry == by) {
		if (move_red < move_blue) { // red 선
			bx -= dx; by -= dy;
		}
		else { // red 후
			rx -= dx; ry -= dy;
		}
	}

	// 분기
	if (!(dx == -1 && dy == 0)) dfs(rx, ry, bx, by, -1, 0, cnt + 1);
	if (!(dx == 1 && dy == 0)) dfs(rx, ry, bx, by, 1, 0, cnt + 1);
	if (!(dx == 0 && dy == -1)) dfs(rx, ry, bx, by, 0, -1, cnt + 1);
	if (!(dx == 0 && dy == 1)) dfs(rx, ry, bx, by, 0, 1, cnt + 1);
}



int main() {
	int rx, ry, bx, by;
	char str[11];

	scanf("%d", &N);
	scanf("%d", &M);

	for (int i = 0; i < N; i++) {
		scanf("%s", str);
		for (int j = 0; j < M; j++) {
			board[i][j] = str[j];
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (board[i][j] == 'R') {
				rx = i;
				ry = j;
			}
			else if (board[i][j] == 'B') {
				bx = i;
				by = j;
			}
			else if (board[i][j] == 'O') {
				ex = i;
				ey = j;
			}
		}
	}
	
	ans = 1000000;
	dfs(rx, ry, bx, by, 0, 0, 0);

	if (ans <= 10) {
		printf("%d", ans);
	}
	else {
		printf("%d", -1);
	}
	
	return 0;
}



