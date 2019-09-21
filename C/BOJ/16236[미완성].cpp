#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;

// N : 공간의 크기
// 0: 빈 칸
// 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
// 9 : 아기 상어의 위치

//더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
//먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
//먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.

int N;
int map[20][20];
int visited[20][20];
int sx, sy, ans;

typedef struct {
	int x;
	int y;
} xy;

bool point_check(int x, int y) {
	return x >= 0 && x < N && y >= 0 && y < N;
}

void visited_init() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			visited[i][j] = false;
		}
	}
}


void bfs(int sx, int sy) {

	// 1. 먹을 물고기 선택
	// 2. 이동, visited 체크
	// 3. 포식, visited 초기화, map 물고기 제거
	
	queue<xy> que;
	int s_size, feed_cnt, cnt;
	xy start = { sx,sy };

	s_size = 2;
	feed_cnt = 0;
	cnt = 0;
	que.push(start);
	visited_init();
	visited[sx][sy] = true;

	while (!que.empty()) {
		int que_size = que.size();

		cout << "cnt " << cnt << endl;
		for (int i = 0; i < que_size; i++) {
			xy node = que.front();
			que.pop();

			cout << "node " << node.x << "," << node.y << endl;

			if (map[node.x][node.y] > 0 && map[node.x][node.y] < s_size) {
				feed_cnt++;

				if (feed_cnt == s_size) {
					feed_cnt = 0;
					s_size++;
				}
				map[node.x][node.y] = 0;
				while (!que.empty()) {
					que.pop();
				}
				visited_init();
				ans = cnt;
			}

			int next_x, next_y;
			next_x = node.x - 1;
			next_y = node.y;
			if (!visited[next_x][next_y] && 
				point_check(next_x, next_y) &&
				map[next_x][next_y] <= s_size) 
			{
				visited[next_x][next_y] = true;
				que.push({next_x, next_y});
			}
			next_x = node.x;
			next_y = node.y - 1;
			if (!visited[next_x][next_y] &&
				point_check(next_x, next_y) &&
				map[next_x][next_y] <= s_size)
			{
				visited[next_x][next_y] = true;
				que.push({ next_x, next_y });
			}
			next_x = node.x + 1;
			next_y = node.y;
			if (!visited[next_x][next_y] &&
				point_check(next_x, next_y) &&
				map[next_x][next_y] <= s_size)
			{
				visited[next_x][next_y] = true;
				que.push({ next_x, next_y });
			}
			next_x = node.x;
			next_y = node.y + 1;
			if (!visited[next_x][next_y] &&
				point_check(next_x, next_y) &&
				map[next_x][next_y] <= s_size)
			{
				visited[next_x][next_y] = true;
				que.push({ next_x, next_y });
			}
		}
		cnt++;
	}


	//int next_x, next_y;
	//next_x = sx - 1;
	//next_y = sy;
	//if (!visited[next_x][next_y] && point_check(next_x, next_y)) {
	//	visited[next_x][next_y] = true;
	//	dfs(next_x, next_y, size, feed_cnt, cnt + 1);
	//}
	//next_x = sx + 1;
	//next_y = sy;
	//if (!visited[next_x][next_y] && point_check(next_x, next_y)) {
	//	visited[next_x][next_y] = true;
	//	dfs(next_x, next_y, size, feed_cnt, cnt + 1);
	//}
	//next_x = sx;
	//next_y = sy - 1;
	//if (!visited[next_x][next_y] && point_check(next_x, next_y)) {
	//	visited[next_x][next_y] = true;
	//	dfs(next_x, next_y, size, feed_cnt, cnt + 1);
	//}
	//next_x = sx;
	//next_y = sy + 1;
	//if (!visited[next_x][next_y] && point_check(next_x, next_y)) {
	//	visited[next_x][next_y] = true;
	//	dfs(next_x, next_y, size, feed_cnt, cnt + 1);
	//}
}


int main() {
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &map[i][j]);
			if (map[i][j] == 9) {
				sx = i;
				sy = j;
			}
		}
	}

	ans = 0;
	bfs(sx, sy);

	printf("%d", ans);
}