// 문제점 : queue에 push전에 flag 설정할 것 -> overflow 방지, 중복 push 방지


#include <iostream>
#include <cstdio>
#include <queue>

// i, j = 1 부터 시작
// [x][y] : 세로가로

using namespace std;

int N, M;
int maze[101][101], xy_cnt[101][101];

int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,-1,1 };

typedef struct {
	int x;
	int y;
} xy;

bool node_end_check(xy node1, xy node2) {
	return node1.x == node2.x && node1.y == node2.y;
}

bool location_check(int cx, int cy) {
	return cx > 0 && cx <= N && cy > 0 && cy <= M;
}

int bfs(int x, int y) {
	int cnt;
	int i, j;
	int cx, cy;
	queue<xy> que;
	xy end, start, next;
	start.x = 1;
	start.y = 1;
	end.x = x;
	end.y = y;

	cnt = 0;
	que.push(start);

	while (!que.empty()) {
		int que_size = que.size();

		cnt++;
		for (i = 0; i < que_size; i++) {
			xy node = que.front();
			que.pop();

			//cout << "node " << node.x << " " << node.y << endl;
			if (node_end_check(node, end)) {
				return cnt;
			}
			for (j = 0; j < 4; j++) {
				cx = node.x + dx[j];
				cy = node.y + dy[j];
				if (location_check(cx, cy) && maze[cx][cy] == 1 
					&& xy_cnt[cx][cy] == 0) {
					xy next = { cx,cy };
					xy_cnt[cx][cy] = cnt;
					que.push(next);
				}
			}
		}
	}

	return -1;
}


int main() {
	int i, j;
	char str[101];
	scanf("%d", &N);
	scanf("%d", &M);

	for (i = 1; i <= N; i++) {
		scanf("%s", str);
		for (j = 1; j <= M; j++) {
			maze[i][j] = str[j-1] - '0';
			xy_cnt[i][j] = 0;
		}
	}

	printf("%d",bfs(N, M));
}

