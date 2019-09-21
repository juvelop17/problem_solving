#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;



// 총 F층
// 현재 S층
// 버튼 2개
// 위로 U층
// 아래로 D층
// G층 도착
// 불가능하면 use the stairs 출력

int F, S, G, U, D;
int button_cnt[1000001];

int bfs() {
	queue<int> que;
	int cnt;
	int next, node;

	cnt = 0;
	que.push(S);
	button_cnt[S] = 0;
	while (!que.empty()) {
		int que_size = que.size();
		
		cnt++;
		for (int i = 0; i < que_size; i++) {
			node = que.front();
			que.pop();

			if (node == G) {
				return button_cnt[node];
			}

			next = node + U;
			if (next <= F && button_cnt[next] == 0 && next != S) {
				button_cnt[next] = cnt;
				que.push(next);
			}

			next = node - D;
			if (next >= 1 && button_cnt[next] == 0 && next != S) {
				button_cnt[next] = cnt;
				que.push(next);
			}
		}
	}

	return -1;
}



int main() {
	int result;

	scanf("%d", &F);
	scanf("%d", &S);
	scanf("%d", &G);
	scanf("%d", &U);
	scanf("%d", &D);

	for (int i = 1; i < 1000001; i++) {
		button_cnt[i] = 0;
	}

	result = bfs();
	if (result != -1) {
		printf("%d", result);
	}
	else {
		printf("use the stairs");
	}
}