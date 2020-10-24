#include <cstdio>
#include <iostream>
#include <queue>


using namespace std;

// l : 한변의 길이
// 범위 : 0 ~ l-1
int l, tc_num;
int tc_value[1000][5], tc_result[1000];
int xy_cnt[300][300];

int dx[8] = {-1,-2,-2,-1,1,2,2,1};
int dy[8] = {-2,-1,1,2,2,1,-1,-2};

typedef struct {
	int x;
	int y;
} xy;

bool xy_check(int cx, int cy) {
	return cx >= 0 && cx < l && cy >= 0 && cy < l;
}

int bfs(xy start, xy end) {
	int i, j, cnt, cx, cy, min;
	queue<xy> que;
	
	que.push(start);
	cnt = 0;
	xy_cnt[start.x][start.y] = 0;
	min = 1000000;

	while (!que.empty()) {
		int que_size = que.size();
		cnt++;
		//cout << "cnt " << cnt << endl;
		for (i = 0; i < que_size; i++) {
			xy node = que.front();
			que.pop();

			//cout << "node " << node.x << " " << node.y << endl;
			if (node.x == end.x &&node.y == end.y) {
				return xy_cnt[end.x][end.y];
			}
			for (j = 0; j < 8; j++) {
				cx = node.x + dx[j];
				cy = node.y + dy[j];
				if (xy_cnt[cx][cy] == 0 && xy_check(cx, cy)) {
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
	int i, j, a, b, c, d;
	xy start, end;

	scanf("%d", &tc_num);

	for (i = 0; i < tc_num; i++) {
		for (int i = 0; i < 300; i++) {
			for (int j = 0; j < 300; j++) {
				xy_cnt[i][j] = 0;
			}
		}

		scanf("%d", &l);
		scanf("%d", &a);
		scanf("%d", &b);
		scanf("%d", &c);
		scanf("%d", &d);
		
		start = { a,b };
		end = { c,d };

		tc_result[i] = bfs(start, end);
	}

	for (i = 0; i < tc_num; i++) {
		printf("%d\n", tc_result[i]);
	}
}
